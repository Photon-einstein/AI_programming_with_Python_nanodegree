# Example 1. Plot a default histogram
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the Pokémon dataset
pokemon = pd.read_csv("pokemon.csv")

# Print the shape of the dataset
print(pokemon.shape)

# Display the first 10 rows of the dataset
print("\nPokemon data, first entries: ", pokemon.head(10))

# Plot a default histogram as shown below:

# Intentionally omitting a semicolon to display the bar width
plt.hist(data=pokemon, x="speed")
plt.title("Default Pokemon speed histogram")
plt.show()

# Example 2. Histogram with fixed number of bins
# Plot a histogram with 20 bins
plt.hist(data=pokemon, x="speed", bins=20)
plt.title("Pokemon speed histogram with 20 bins")
plt.show()

# Example 3. Histogram with dynamic number of bins
# Create bins with a step size of 5, plus 5 to create the last bin
bins = np.arange(0, pokemon["speed"].max(), 5)

# Plot a histogram using the defined bins
plt.hist(data=pokemon, x="speed", bins=bins)
plt.title("Pokemon speed histogram with defined bins")
plt.show()

# Example 4. Plot the similar histogram with Seaborn’s histplot()
# Plot a histogram with KDE (Kernel Density Estimate) line
sb.displot(data=pokemon, x="speed", kde=True, stat="density", bins=20)
plt.title("Pokemon speed histogram with seaborn histplot with KDE line")
plt.show()

# Plot a histogram without the KDE line
sb.histplot(data=pokemon, x="speed")
plt.title("Pokemon speed histogram with seaborn histplot without KDE line")
plt.show()

# Example 5:
# Define bin edges for the histogram based on the 'speed' column
bin_edges = np.arange(0, pokemon["speed"].max() + 1, 5)

# Plot the distribution of the 'speed' column using seaborn
sb.histplot(data=pokemon, x="speed", bins=bin_edges, alpha=1)
plt.title("Distribution of the 'speed' column using seaborn")
plt.show()

# Example 5. Plot two histograms side-by-side
# Resize the chart, and have two plots side-by-side
# Set a larger figure size for subplots
plt.figure(figsize=[20, 5])

# Histogram on the left: example of too-large bin size
# 1 row, 2 columns, subplot 1
plt.subplot(1, 2, 1)
bins = np.arange(0, pokemon["speed"].max() + 4, 4)
plt.hist(data=pokemon, x="speed", bins=bins)

# Histogram on the right: example of too-small bin size
# 1 row, 2 columns, subplot 2
plt.subplot(1, 2, 2)
bins = np.arange(0, pokemon["speed"].max() + 0.25, 0.25)
plt.hist(data=pokemon, x="speed", bins=bins)
plt.title("Two histograms side-by-side")
plt.show()
