import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the Pokémon dataset
pokemon = pd.read_csv("pokemon.csv")

# Create a new figure
fig = plt.figure()

# Example 2. Demonstrate figure.add_axes() and axes.hist()
# The argument of add_axes represents the dimensions [left, bottom, width, height] of the new axes.
# All quantities are in fractions of figure width and height.
ax = fig.add_axes([0.125, 0.125, 0.775, 0.755])
ax.hist(data=pokemon, x="speed")
plt.title("Pokemon's speed histogram")
plt.show()


# Example 2. Use axes with seaborn.countplot()
fig = plt.figure()
ax = fig.add_axes([0.125, 0.125, 0.775, 0.755])
base_color = sb.color_palette()[0]
sb.countplot(data=pokemon, x="generation_id", color=base_color, ax=ax)
plt.title("Pokemon's generation id histogram")
plt.show()

# Example 3. Sub-plots
# Resize the chart, and have two plots side-by-side
# set a larger figure size for subplots
# sets the width and height of the overall figure to 20 inches by 5 inches
plt.figure(figsize=[20, 5])

# histogram on left, example of too-large bin size
# 1 row, 2 cols, subplot 1
plt.subplot(1, 2, 1)
bins = np.arange(0, pokemon["speed"].max() + 4, 4)
plt.hist(data=pokemon, x="speed", bins=bins)
plt.title("Pokemon's speed histogram, 4 width bins")

# histogram on right, example of too-small bin size
plt.subplot(1, 2, 2)  # 1 row, 2 cols, subplot 2
bins = np.arange(0, pokemon["speed"].max() + 1 / 4, 1 / 4)
plt.hist(data=pokemon, x="speed", bins=bins)
plt.title("Pokemon's speed histogram, 0.25 width bins")
plt.show()

# Example 4. Demonstrate pyplot.sca() and pyplot.text() to generate a grid of subplots
fig, axes = plt.subplots(3, 4)  # grid of 3x4 subplots
axes = axes.flatten()  # reshape from 3x4 array into 12-element vector
for i in range(12):
    plt.sca(axes[i])  # set the current Axes
    plt.text(
        0.5, 0.5, i + 1
    )  # print conventional subplot index number to middle of Axes
plt.show()
