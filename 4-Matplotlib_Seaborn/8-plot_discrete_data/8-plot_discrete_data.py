import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

die_rolls = pd.read_csv("die-rolls.csv")

# A fair dice has six-faces having numbers [1-6].
# There are 100 dices, and two trials were conducted.
# In each trial, all 100 dices were rolled down, and the outcome [1-6] was recorded.
# The `Sum` column represents the sum of the outcomes in the two trials, for each given dice.
print("\nFirst entries of die-rolls table:\n", die_rolls.head(10), "\n")

# Example 1. Shifting the edges of the bars can remove ambiguity in the case of discrete data
plt.figure(figsize = [20, 5])

# Histogram on the left, bin edges on integers
plt.subplot(1, 2, 1)
bin_edges = np.arange(2, 12 + 1.1, 1) # note `+1.1`, see below
plt.hist(data=die_rolls, x='Sum', bins=bin_edges)
plt.xticks(np.arange(2, 12 + 1, 1))
plt.title("Histogram with bin edges on integers")

# Histogram on the right, bin edges between integers
plt.subplot(1, 2, 2)
bin_edges = np.arange(1.5, 12.5 + 1, 1)
plt.hist(data=die_rolls, x='Sum', bins=bin_edges)
plt.xticks(np.arange(2, 12 + 1, 1))
plt.title("Histogram with bin edges between integers")
plt.show()

# Example 2. Making gaps between individual bars
bin_edges = np.arange(1.5, 12.5 + 1, 1)
plt.hist(data=die_rolls, x='Sum', bins=bin_edges, rwidth=0.7)
plt.xticks(np.arange(2, 12 + 1, 1))
plt.title("Histogram with bin edges between integers and 30% gaps")
plt.show()