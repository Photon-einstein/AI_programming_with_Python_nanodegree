# Example 1. Create a vertical bar chart using Seaborn, with default colors

# Necessary imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Read the csv file, and check its top 10 rows
pokemon = pd.read_csv('pokemon.csv')
print(pokemon.shape)
print(pokemon.head(10))

# A semicolon (;) at the end of the statement will suppress printing the plotting information
sb.countplot(data=pokemon, x='generation_id')
plt.title('Pokemon Count by Generation (Default Colors)')
plt.show()

# Example 2. Create a vertical bar chart using Seaborn, with a uniform single color
# The `color_palette()` returns the the current / default palette as a list of RGB tuples. 
# Each tuple consists of three digits specifying the red, green, and blue channel values to specify a color. 
# Choose the first tuple of RGB colors
base_color = sb.color_palette()[0]

# Use the `color` argument
sb.countplot(data=pokemon, x='generation_id', color=base_color)
plt.title('Pokemon Count by Generation (Uniform Color)')
plt.show()

# Example 3. Create a vertical bar chart using Matplotlib, with a uniform single color
# Return the Series having unique values
x = pokemon['generation_id'].unique()

# Return the Series having frequency count of each unique value
y = pokemon['generation_id'].value_counts(sort=False)

plt.bar(x, y)

# Labeling the axes
plt.xlabel('generation_id')
plt.ylabel('count')
plt.title('Pokemon Count by Generation (Matplotlib)')

# Display the plot
plt.show()

# Example 4. Static and dynamic ordering of the bars in a bar chart using seaborn.countplot()
# Static-ordering the bars
sb.countplot(data=pokemon, x='generation_id', color=base_color, order=[5,1,3,4,2,7,6])
plt.title('Pokemon Count by Generation (Static Custom Order)')
plt.show()

# Dynamic-ordering the bars
# The order of the display of the bars can be computed with the following logic.
# Count the frequency of each unique value in the 'generation_id' column, and sort it in descending order
# Returns a Series
freq = pokemon['generation_id'].value_counts()

# Get the indexes of the Series
gen_order = freq.index

# Plot the bar chart in the decreasing order of the frequency of the `generation_id`
sb.countplot(data=pokemon, x='generation_id', color=base_color, order=gen_order)
plt.title('Pokemon Count by Generation (Sorted by Frequency)')
plt.show()

# Example 5. Rotate the category labels (not axes)
# Plot the Pokemon type on a Vertical bar chart
sb.countplot(data=pokemon, x='type_1', color=base_color);

# Use xticks to rotate the category labels (not axes) counter-clockwise
plt.xticks(rotation=90)
plt.show()

# Example 6. Rotate the axes clockwise
# Plot the Pokemon type on a Horizontal bar chart
type_order = pokemon['type_1'].value_counts().index
sb.countplot(data=pokemon, y='type_1', color=base_color, order=type_order)
plt.show()
