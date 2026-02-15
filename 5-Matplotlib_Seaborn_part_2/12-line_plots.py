import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

# Example 1
plt.errorbar(data=fuel_econ, x="displ", y="comb")
plt.xticks(rotation=15)
plt.ylabel("Avg. Combined Fuel Efficiency (mpg)")
plt.show()

# Example 2.
## Set a number of bins into which the data will be grouped.
## Set bin edges, and compute center of each bin
bin_edges = np.arange(0.6, 7 + 0.2, 0.2)
bin_centers = bin_edges[:-1] + 0.1

## Cut the bin values into discrete intervals. Returns a Series object.
displ_binned = pd.cut(fuel_econ["displ"], bin_edges, include_lowest=True)
print("\n", displ_binned)

## For the points in each bin, we compute the mean and standard error of the mean.
comb_mean = fuel_econ["comb"].groupby(displ_binned, observed=False).mean()
comb_std = fuel_econ["comb"].groupby(displ_binned, observed=False).std()

## Plot the summarized data
plt.errorbar(x=bin_centers, y=comb_mean, yerr=comb_std)
plt.xticks(rotation=15)
plt.ylabel("Avg. Combined Fuel Efficiency (mpg)")
plt.show()

# Example 3.
## compute statistics in a rolling window
df_window = fuel_econ[["displ", "comb"]].sort_values("displ").rolling(15)
x_winmean = df_window.mean()["displ"]
y_median = df_window.median()["comb"]
y_q1 = df_window.quantile(0.25)["comb"]
y_q3 = df_window.quantile(0.75)["comb"]

## plot the summarized data
base_color = sb.color_palette()[0]
line_color = sb.color_palette("dark")[0]
plt.scatter(data=fuel_econ, x="displ", y="comb")
plt.errorbar(x=x_winmean, y=y_median, c=line_color)
plt.errorbar(x=x_winmean, y=y_q1, c=line_color, linestyle="--")
plt.errorbar(x=x_winmean, y=y_q3, c=line_color, linestyle="--")

plt.xlabel("Displacement (l)")
plt.ylabel("Combined Fuel Efficiency (mpg)")
plt.show()


def freq_poly(x, bins=10, **kwargs):
    """Custom frequency polygon / line plot code."""
    # set bin edges if none or int specified
    if type(bins) == int:
        bins = np.linspace(x.min(), x.max(), bins + 1)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2

    # compute counts
    data_bins = pd.cut(x, bins, right=False, include_lowest=True)
    counts = x.groupby(data_bins).count()

    # create plot
    plt.errorbar(x=bin_centers, y=counts, **kwargs)


bin_edges = np.arange(-3, fuel_econ["comb"].max() + 1 / 3, 1 / 3)
g = sb.FacetGrid(data=fuel_econ)
g.map(freq_poly, "comb", bins=bin_edges)
g.add_legend()
plt.show()
