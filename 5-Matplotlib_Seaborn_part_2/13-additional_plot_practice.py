# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


from solutions_biv import additionalplot_solution_1, additionalplot_solution_2


# We'll continue to make use of the fuel economy dataset in this workspace.


fuel_econ = pd.read_csv("fuel_econ.csv")
print("fuel_econ table, first entries:\n", fuel_econ.head())


# ### **Task 1**:
# Plot the distribution of combined fuel mileage (column 'comb', in miles per gallon)
# by manufacturer (column 'make'), for all manufacturers with at least eighty cars in
# the dataset.
# Consider which manufacturer order will convey the most information when constructing your final plot.
#
# **Hint**: Completing this exercise will take multiple steps! Add additional code cells as needed in order to achieve the goal.

# YOUR CODE HERE
THRESHOLD = 80
make_frequency = fuel_econ["make"].value_counts()
idx = np.sum(make_frequency > THRESHOLD)
most_makes = make_frequency.index[:idx]
fuel_econ_sub = fuel_econ.loc[fuel_econ["make"].isin(most_makes)]
make_means = fuel_econ_sub.groupby("make").mean(numeric_only=True)
comb_order = make_means.sort_values("comb", ascending=False).index

# plotting
g = sb.FacetGrid(
    data=fuel_econ_sub, col="make", col_wrap=6, height=2, col_order=comb_order
)
# try sb.distplot instead of plt.hist to see the plot in terms of density!
g.map(plt.hist, "comb", bins=np.arange(12, fuel_econ_sub["comb"].max() + 2, 2))
g.set_titles("{col_name}")
plt.show()

# run this cell to check your work against ours
# additionalplot_solution_1()


# ### **Task 2**:
# Continuing on from the previous task, plot the mean fuel efficiency for each manufacturer with at least 80 cars in the dataset.

# YOUR CODE HERE
base_color = sb.color_palette()[0]
# plotting
base_color = sb.color_palette()[0]
sb.barplot(
    data=fuel_econ_sub,
    x="comb",
    y="make",
    color=base_color,
    order=comb_order,
    errorbar="sd",
)
plt.xlabel("Average Combined Fuel Eff. (mpg)")
plt.show()

# run this cell to check your work against ours
# additionalplot_solution_2()
