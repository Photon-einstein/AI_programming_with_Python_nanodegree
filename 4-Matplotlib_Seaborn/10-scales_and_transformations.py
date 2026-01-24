import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv("pokemon.csv")
pokemon.head(10)

plt.figure(figsize=[20, 5])

## HISTOGRAM ON LEFT: full data without scaling
plt.subplot(1, 2, 1)
plt.hist(data=pokemon, x="weight")
## Display a label on the x-axis
plt.xlabel("Initial plot with original data")

## HISTOGRAM ON RIGHT
plt.subplot(1, 2, 2)

## Get the ticks for bins between [0 - maximum weight]
bins = np.arange(0, pokemon["weight"].max() + 40, 40)
plt.hist(data=pokemon, x="weight", bins=bins)

## The argument in the xscale() represents the axis scale type to apply.
## The possible values are: {"linear", "log", "symlog", "logit", ...}
## Refer - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xscale.html
plt.xscale("log")
plt.xlabel("The x-axis limits NOT are changed. They are only scaled to log-type")
plt.show()

## Describe the data
print(pokemon["weight"].describe())

# Example 2 - Scale the x-axis to log-type, and change the axis limit.
## Transform the describe() to a scale of log10
## Documentation: [numpy `log10`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log10.html)
print("\n", np.log10(pokemon["weight"].describe()))

## Axis transformation
## Bin size
bins = 10 ** np.arange(-1, 3 + 0.1, 0.1)
plt.hist(data=pokemon, x="weight", bins=bins)

## The argument in the xscale() represents the axis scale type to apply.
## The possible values are: {"linear", "log", "symlog", "logit", ...}
plt.xscale("log")

## Apply x-axis label
## Documentation: [matplotlib `xlabel`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html))
plt.xlabel("x-axis limits are changed, and scaled to log-type")
plt.show()

# Example 3 - Scale the x-axis to log-type, change the axis limits, and increase the x-ticks

## Get the ticks for bins between [0 - maximum weight]
bins = 10 ** np.arange(-1, 3 + 0.1, 0.1)

## Generate the x-ticks you want to apply
ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
## Convert ticks into string values, to be displayed along the x-axis
labels = ["{}".format(v) for v in ticks]

## Plot the histogram
plt.hist(data=pokemon, x="weight", bins=bins)

## The argument in the xscale() represents the axis scale type to apply.
## The possible values are: {"linear", "log", "symlog", "logit", ...}
plt.xscale("log")

## Apply x-ticks
plt.xticks(ticks, labels)
plt.show()


# Example 4. Custom scaling the given data Series, instead of using the built-in log scale
def sqrt_trans(x, inverse=False):
    """transformation helper function"""
    if not inverse:
        return np.sqrt(x)
    else:
        return x**2


## Bin resizing, to transform the x-axis
bin_edges = np.arange(0, sqrt_trans(pokemon["weight"].max()) + 1, 1)

## Plot the scaled data
plt.hist(pokemon["weight"].apply(sqrt_trans), bins=bin_edges)

## Identify the tick-locations
tick_locs = np.arange(0, sqrt_trans(pokemon["weight"].max()) + 10, 10)

## Apply x-ticks
plt.xticks(tick_locs, sqrt_trans(tick_locs, inverse=True).astype(int))
plt.show()
