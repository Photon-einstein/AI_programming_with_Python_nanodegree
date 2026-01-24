# Prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# The `solutions_univ.py` is a Python file available in the Notebook server that contains solution to the TO DO tasks.
# The solution to each task is present in a separate function in the `solutions_univ.py` file. 
# Do not refer to the file untill you attempt to write code yourself. 
from solutions_univ import histogram_solution_1


# ### About the Dataset
# We'll continue working with the Pokémon dataset in this workspace. The data was assembled from the database of information found in this [GitHub repository](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv).
# 

pokemon = pd.read_csv('data/pokemon.csv')
print("\nPokemon table, first entries:\n", pokemon.head())


# ### **TO DO Task**
# Pokémon have a number of different statistics that describe their combat capabilities. Here, create a _histogram_ that depicts the distribution of 'special-defense' values taken. 
# 
# **Hint**: Try playing around with different bin width sizes to see what best depicts the data.

# YOUR CODE HERE
# Create bins with a step size of 5, plus 5 to create the last bin
bins = np.arange(0, pokemon["speed"].max(), 5)
plt.hist(data=pokemon, x="special-defense", bins=bins)
plt.title("Pokemon's special defense histogram")
plt.show()

# ### Expected Output
# **Your visualization does not need to be exactly the same as ours, but it should be able to come up with the same conclusions.**

# run this cell to check your work against ours
print()
histogram_solution_1()
