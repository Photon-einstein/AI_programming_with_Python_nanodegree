# Example 1. Violin versus Box plot

# Step 1. Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Step 2. Load data
fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())

# Step 3. Convert the "VClass" column from a plain object type into an ordered categorical type
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

# Use pandas.astype() to convert the "VClass" column from a plain object type into an ordered categorical type
fuel_econ["VClass"] = fuel_econ["VClass"].astype(vclasses)

# Step 4.  TWO PLOTS IN ONE FIGURE
plt.figure(figsize=[16, 5])  # 16 inches width x 5 inches height
base_color = sb.color_palette()[0]

# LEFT plot: violin plot
plt.subplot(1, 2, 1)
# Let's return the axes object
ax1 = sb.violinplot(
    data=fuel_econ, x="VClass", y="comb", color=base_color, inner="quartile"
)
plt.xticks(rotation=15)
plt.title("Violin plot: Vehicle class vs fuel efficiency")

# RIGHT plot: box plot
plt.subplot(1, 2, 2)
sb.boxplot(data=fuel_econ, x="VClass", y="comb", color=base_color)
plt.xticks(rotation=15)
plt.ylim(ax1.get_ylim())  # set y-axis limits to be same as left plot
plt.title("Box plot: Vehicle class vs fuel efficiency")
plt.show()

# Example 2. Horizontal box plot
sb.boxplot(data=fuel_econ, y="VClass", x="comb", color=base_color)
plt.title("Box plot: Fuel efficiency vs Vehicle class")
plt.show()

# Example 3. Violin plot with quartile information in the middle
base_color = sb.color_palette()[0]
sb.violinplot(data=fuel_econ, x="VClass", y="comb", color=base_color, inner="quartile")
plt.xticks(rotation=30)
plt.title("Box plot with quartile info: Vehicle class vs fuel efficiency")
plt.show()
