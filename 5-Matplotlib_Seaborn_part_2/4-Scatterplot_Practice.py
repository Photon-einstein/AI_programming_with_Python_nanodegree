import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from solutions_biv import scatterplot_solution_1, scatterplot_solution_2

# In this workspace, you'll make use of this data set describing various car attributes,
# such as fuel efficiency. The cars in this dataset represent about 3900 sedans tested
# by the EPA from 2013 to 2018. This dataset is a trimmed-down version of the data found
# [here](https://video.udacity-data.com/topher/2018/April/5ac2907f_fuel-econ/fuel-econ.csv).

fuel_econ = pd.read_csv("fuel_econ.csv")
print("\nFirst entries of the fuel_econ table:\n", fuel_econ.head())
print(fuel_econ.describe())

# ### **TO DO 1**:
# Let's look at the relationship between fuel mileage ratings for city vs. highway driving,
# as stored in the 'city' and 'highway' variables (in miles per gallon, or mpg).
# **Use a _scatter plot_ to depict the data.**
# 1. What is the general relationship between these variables?
# 2. Are there any points that appear unusual against these trends?

# Scatter plot
plt.scatter(data=fuel_econ, x="city", y="highway", alpha=1 / 8)
plt.xlabel("City consumption (mpg)")
plt.ylabel("Highway consumption (mpg)")
plt.title("City vs Highway consumption (mgp)")
plt.show()

# ### Expected Output
scatterplot_solution_1()

# ### **TO DO 2**:
# Let's look at the relationship between two other numeric variables. How does the engine size
# relate to a car's CO2 footprint? The 'displ' variable has the former (in liters), while the
# 'co2' variable has the latter (in grams per mile). **Use a heat map to depict the data.
# ** How strong is this trend?

# ### Expected Output
bins_x = np.arange(0.6, fuel_econ["displ"].max() + 0.4, 0.4)
bins_y = np.arange(0, fuel_econ["co2"].max() + 50, 50)

plt.hist2d(
    data=fuel_econ,
    x="displ",
    y="co2",
    cmin=0.5,
    cmap="viridis_r",
    bins=[bins_x, bins_y],
)
plt.colorbar()
plt.xlabel("Displacement (L)")
plt.ylabel("CO2(g/m)")
plt.title("Heat Map: Displacement vs CO2 production")
plt.show()

# run this cell to check your work against ours
scatterplot_solution_2()
