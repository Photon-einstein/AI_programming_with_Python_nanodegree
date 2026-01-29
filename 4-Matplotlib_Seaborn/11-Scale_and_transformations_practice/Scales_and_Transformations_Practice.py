# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from solutions_univ import scales_solution_1, scales_solution_2

# Once again, we make use of the Pokémon data for this exercise.
pokemon = pd.read_csv('../pokemon.csv')
print("\nPokemon table, first entries:\n", pokemon.head())


# ## TO DO **Task 1**
# There are also variables in the dataset that don't have anything to do with the game mechanics, and are just there for flavor. Try plotting the distribution of Pokémon heights (given in meters). For this exercise, experiment with different axis limits as well as bin widths to see what gives the clearest view of the data.

print("\n", pokemon.describe())

# YOUR CODE HERE
bins = np.arange(0, pokemon["height"].max() + 0.2, 0.2)
# Plot the histogram for the height column
plt.hist(data=pokemon, x="height", bins=bins)
plt.title("Histogram of Pokemon's height (m)")
plt.xlabel("Height (m)")
plt.xlim((0, 6))
plt.show()

# ## Expected Output: TO DO Task 1


# run this cell to check your work against ours
scales_solution_1()


# ## TO DO **Task 2**
# In this task, you should plot the distribution of Pokémon weights (given in kilograms). Due to the very large range of values taken, you will probably want to perform an _axis transformation_ as part of your visualization workflow.


# YOUR CODE HERE
print("\n", np.log10(pokemon["weight"].describe())) # [-1, 3]

bins = 10 ** np.arange(-1, 3 + 0.1, 0.1)
plt.hist(data=pokemon, x="weight", bins=bins)
plt.xscale("log")

# ## Expected Output: TO DO Task 2
plt.title("Histogram of Pokemon's weight")
plt.xlabel("Weight (kg) [log₁₀ scale]")
ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
labels = ["{}".format(v) for v in ticks]
plt.xticks(ticks, labels)
plt.show()


# run this cell to check your work against ours
scales_solution_2()
