import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

base_color = sb.color_palette()[0]
sb.barplot(data=fuel_econ, x="VClass", y="comb", color=base_color)
plt.xticks(rotation=15)
plt.ylabel("Avg. Combined Fuel Efficiency (mpg)")
# Try these additional arguments

# Hide error bars
sb.barplot(
    data=fuel_econ, x="VClass", y="comb", color=base_color, err_kws={"linewidth": 0}
)

# Show error bars based on standard deviation
sb.barplot(data=fuel_econ, x="VClass", y="comb", color=base_color, errorbar="sd")
plt.show()

# Example 2.
sb.pointplot(
    data=fuel_econ, x="VClass", y="comb", color=base_color, ci="sd", linestyles=""
)
plt.xticks(rotation=15)
plt.ylabel("Avg. Combined Fuel Efficiency (mpg)")
plt.show()

# Example 3. Bringing a few charts together
plt.figure(figsize=[20, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 3, 1)
sb.violinplot(data=fuel_econ, x="VClass", y="comb", inner=None, color=base_color)
plt.xticks(rotation=45)  # include label rotation due to small subplot size

# center plot: box plot
plt.subplot(1, 3, 2)
sb.boxplot(data=fuel_econ, x="VClass", y="comb", color=base_color)
plt.xticks(rotation=45)

# right plot: adapted bar chart
plt.subplot(1, 3, 3)
sb.barplot(data=fuel_econ, x="VClass", y="comb", color=base_color)
plt.xticks(rotation=45)
plt.show()
