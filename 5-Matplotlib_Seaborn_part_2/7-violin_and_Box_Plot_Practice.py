import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from solutions_biv import violinbox_solution_1

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

# ### Preparatory Step
# The cars in this dataset are categorized into one of five different vehicle classes based on size.
# Starting from the smallest, they are:
# `{Minicompact Cars, Subcompact Cars, Compact Cars, Midsize Cars, and Large Cars}`.
#
# ### **TO DO**:
# 1. What is the relationship between the size of a car and the size of its engine?
# The vehicle classes can be found in the `VClass` column, while the engine sizes are
# in the `displ` column (in liters).
#
# **Hint**: Make sure that the order of vehicle classes makes sense in your plot!

# YOUR CODE HERE
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
# Use pandas.astype() to convert the "VClass" column from a plain object type into an ordered categorical type
fuel_econ["VClass"] = fuel_econ["VClass"].astype(vclasses)
base_color = sb.color_palette()[0]
ax1 = sb.violinplot(
    data=fuel_econ, x="VClass", y="displ", color=base_color, inner="box"
)
plt.xticks(rotation=15)
plt.xlabel("Vehicle class")
plt.ylabel("Engine size (L)")
plt.title("Violin plot: Vehicle class vs Engine size")
plt.show()

# ### Expected Output

# run this cell to check your work against ours
violinbox_solution_1()
