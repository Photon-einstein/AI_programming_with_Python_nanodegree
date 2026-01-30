import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pokemon = pd.read_csv("pokemon.csv")
pokemon.head(10)

# The pokemon dataset is available to download at the bottom of this page.
# The kind argument can take any one value from {“hist”, “kde”, “ecdf”}.
sb.displot(pokemon['speed'], kind='hist');
# Use the 'kde' kind for kernel density estimation
#sb.displot(pokemon['speed'], kind='kde');
plt.title("Pokemon's speed histogram")
plt.show()

# Example 2. Demonstrating kdeplot() and rugplot() to plot the KDE.

data = [0.0, 3.0, 4.5, 8.0]
plt.figure(figsize=[12, 5])

# Left plot: Showing kde lumps with the default settings
plt.subplot(1, 3, 1)
sb.rugplot(data, color='r')
sb.kdeplot(data)
plt.ylim(0, 0.11)
plt.title("Default KDE")

# Central plot: KDE with narrow bandwidth to show individual probability lumps
plt.subplot(1, 3, 2)
sb.rugplot(data, color='r')
sb.kdeplot(data, bw_adjust=1/3)
plt.ylim(0, 0.17)
plt.title("Narrow Bandwidth")

# Right plot: Choosing a different, triangular kernel function (lump shape)
plt.subplot(1, 3, 3)
sb.rugplot(data, color='r')
sb.kdeplot(data, bw_adjust=1/5)  # Removed kernel parameter
plt.ylim(0, 0.21)
plt.title("Very Narrow Bandwidth")

# Adjust subplot layout to prevent overlap
plt.tight_layout()

plt.show()