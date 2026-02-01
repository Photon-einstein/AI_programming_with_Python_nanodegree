# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from solutions_biv import categorical_solution_1

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

# ###  **TO DO**
# Use a plot to explore whether or not there are differences in recommended
# fuel type depending on the vehicle class. Only investigate the difference
# between the two main fuel types found in the 'fuelType' variable:
# Regular Gasoline and Premium Gasoline.
# (The other fuel types represented in the dataset are of much lower frequency
# compared to the main two, that they'll be more distracting than informative.)
#
#
# **Note**: The dataset as provided does not retain any of the sorting of the
# 'VClass' variable, so you will also need to copy over any code you used
# previously to sort the category levels.

# YOUR CODE HERE
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
fuel_econ_sub = fuel_econ.loc[
    fuel_econ["fuelType"].isin(["Premium Gasoline", "Regular Gasoline"])
]
print("\nFuel type column:\n", fuel_econ_sub)
# Step 3. Plot the bar chart
sb.countplot(data=fuel_econ_sub, x="VClass", hue="fuelType")
plt.xticks(rotation=15)
plt.xlabel("Vehicle class clustered by fuel type")
plt.title("Cluster bar plot: Vehicle by fuel type")
plt.show()
# ### Expected Output


# run this cell to check your work against ours
categorical_solution_1()
