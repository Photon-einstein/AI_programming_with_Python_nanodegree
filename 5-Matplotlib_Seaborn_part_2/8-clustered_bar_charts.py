import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

# Example 1. Plot a Bar chart between two qualitative variables
# Preparatory Step 1 - Convert the "VClass" column from a plain object type into an ordered categorical type
# Types of sedan cars
sedan_classes = [
    "Minicompact Cars",
    "Subcompact Cars",
    "Compact Cars",
    "Midsize Cars",
    "Large Cars",
]

# Returns the types for sedan_classes with the categories and orderliness
# Refer - https://pandas.pydata.org/pandas-docs/version/2.1.3/reference/api/pandas.CategoricalDtype.html
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_classes)

# Use pandas.astype() to convert the "VClass" column from a plain object type into an ordered categorical type
fuel_econ["VClass"] = fuel_econ["VClass"].astype(vclasses)

# Preparatory Step 2 - Add a new column for transmission type - Automatic or Manual
# The existing `trans` column has multiple sub-types of Automatic and Manual.
# But, we need plain two types, either Automatic or Manual. Therefore, add a new column.

# The Series.apply() method invokes the `lambda` function on each value of `trans` column.
# In python, a `lambda` function is an anonymous function that can have only one expression.
fuel_econ["trans_type"] = fuel_econ["trans"].apply(lambda x: x.split()[0])
print(
    "\nFirst entries of the fuel_econ table with new trans_type column:\n",
    fuel_econ.head(),
)

# Step 3. Plot the bar chart
sb.countplot(data=fuel_econ, x="VClass", hue="trans_type")
plt.xticks(rotation=15)
plt.xlabel("Vehicle class clustered by trans type")
plt.title("Cluster bar plot: Vehicle by trans type")
plt.show()

# Alternative Approach
# Example 2. Plot a Heat Map between two qualitative variables
# Step 1 - Get the data into desirable format - a DataFrame
# Use group_by() and size() to get the number of cars and each
# combination of the two variable levels as a pandas Series
ct_counts = fuel_econ.groupby(["VClass", "trans_type"]).size()
print("\n", ct_counts)

# Use Series.reset_index() to convert a series into a dataframe object
ct_counts = ct_counts.reset_index(name="count")
# Use DataFrame.pivot() to rearrange the data, to have vehicle class on rows
ct_counts = ct_counts.pivot(index="VClass", columns="trans_type", values="count")

print("\n", ct_counts)

# Step 2 - Plot the heatmap
sb.heatmap(ct_counts)
plt.title("Heat map: VCass vs trans_type")
plt.show()

# Example 3. Additional Variation
sb.heatmap(ct_counts, annot=True, fmt="d")
plt.title("Heat map: VCass vs trans_type with annotations")
plt.show()
