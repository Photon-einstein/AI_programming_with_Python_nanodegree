import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())

# Example 1. Violin plot for plotting a Quantitative variable
# (fuel efficiency) versus Qualitative variable (vehicle class)
# Types of sedan cars
sedan_classes = [
    "Minicompact Cars",
    "Subcompact Cars",
    "Compact Cars",
    "Midsize Cars",
    "Large Cars",
]

# Returns the types for sedan_classes with the categories and orderliness
# Refer - https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.api.types.CategoricalDtype.html
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_classes)

# Use pandas.astype() to convert the "VClass" column from a plain object
# type into an ordered categorical type
fuel_econ["VClass"] = fuel_econ["VClass"].astype(vclasses)

sb.violinplot(data=fuel_econ, x="VClass", y="comb")
plt.xlabel("Vehicle class")
plt.ylabel("Fuel efficiency")
plt.title("Violin plot: Vehicle class vs fuel efficiency")
plt.show()

# Example 2. Violin plot without datapoints in the violin interior
base_color = sb.color_palette()[0]

# The "inner" argument represents the datapoints in the violin interior.
# It can take any value from {“box”, “quartile”, “point”, “stick”, None}
# If "box", it draws a miniature boxplot.
sb.violinplot(data=fuel_econ, x="VClass", y="comb", color=base_color, inner=None)
plt.xticks(rotation=15)
plt.xlabel("Vehicle class")
plt.ylabel("Fuel efficiency")
plt.title("Violin plot: Vehicle class vs fuel efficiency")
plt.show()

# Example 3: Violin plot horizontal
sb.violinplot(data=fuel_econ, y="VClass", x="comb", color=base_color, inner="box")
plt.xlabel("Vehicle class")
plt.ylabel("Fuel efficiency")
plt.title("Violin plot: Vehicle class vs fuel efficiency")
plt.show()
