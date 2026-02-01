import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Example 1. Default heat plot using Matplotlib.pyplot.hist2d() function
# TO DO: Necessary import

# Read the CSV file
fuel_econ = pd.read_csv("fuel_econ.csv")
fuel_econ.head(10)


plt.figure(figsize=[18, 6])  # 18 inches width x 6 inches height

# PLOT ON LEFT
plt.subplot(1, 2, 1)
sb.regplot(
    data=fuel_econ,
    x="displ",
    y="comb",
    x_jitter=0.04,
    scatter_kws={"alpha": 1 / 10},
    fit_reg=False,
)
plt.xlabel("Displacement (L)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Scatter plot: Displacement vs Combined Fuel Eff")

# PLOT ON RIGHT
plt.subplot(1, 2, 2)
plt.hist2d(data=fuel_econ, x="displ", y="comb")
plt.colorbar()
plt.xlabel("Displacement (1)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Heat Map: Displacement vs Combined Fuel Eff")
plt.show()

# Example 2. Heat plot - Set a minimum bound on counts and a reverse color map
# Use cmin to set a minimum bound of counts
# Use cmap to reverse the color map.
plt.hist2d(data=fuel_econ, x="displ", y="comb", cmin=0.5, cmap="viridis_r")
plt.colorbar()
plt.xlabel("Displacement (1)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Heat Map: Displacement vs Combined Fuel Eff, reverse color map")
plt.show()

# Example 3. Heat plot - Specify bin edges
# Specify bin edges
bins_x = np.arange(0.6, 7 + 0.3, 0.3)
bins_y = np.arange(12, 58 + 3, 3)

plt.hist2d(
    data=fuel_econ,
    x="displ",
    y="comb",
    cmin=0.5,
    cmap="viridis_r",
    bins=[bins_x, bins_y],
)
plt.colorbar()
plt.xlabel("Displacement (1)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Heat Map: Displacement vs Combined Fuel Eff, specify bin edges")
plt.show()

# Example 4. Add text annotation on each cell using pyplot.text() function
# Specify bin edges
bins_x = np.arange(0.6, 7 + 0.7, 0.7)
bins_y = np.arange(12, 58 + 7, 7)
# Use cmin to set a minimum bound of counts
# Use cmap to reverse the color map.
h2d = plt.hist2d(
    data=fuel_econ,
    x="displ",
    y="comb",
    cmin=0.5,
    cmap="viridis_r",
    bins=[bins_x, bins_y],
)

plt.colorbar()
plt.xlabel("Displacement (1)")
plt.ylabel("Combined Fuel Eff. (mpg)")

# Select the bi-dimensional histogram, a 2D array of samples x and y.
# Values in x are histogrammed along the first dimension and
# values in y are histogrammed along the second dimension.
counts = h2d[0]

# Add text annotation on each cell
# Loop through the cell counts and add text annotations for each
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        c = counts[i, j]
        if c >= 100:  # increase visibility on darker cells
            plt.text(
                bins_x[i] + 0.5,
                bins_y[j] + 0.5,
                int(c),
                ha="center",
                va="center",
                color="white",
            )
        elif c > 0:
            plt.text(
                bins_x[i] + 0.5,
                bins_y[j] + 0.5,
                int(c),
                ha="center",
                va="center",
                color="black",
            )
plt.title("Heat Map: Displacement vs Combined Fuel Eff with text annotations")
plt.show()
