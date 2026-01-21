import matplotlib.pyplot as plt
import pandas as pd

pokemon = pd.read_csv('pokemon.csv')
pokemon.head()

# Example 1. Plot a simple Pie chart
# Use the same pokemon dataset
sorted_counts = pokemon['generation_id'].value_counts()
new_label = ['gen5', 'gen1', 'gen3', 'gen4', 'gen2', 'gen7', 'gen6']

#plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90, counterclock = False);
plt.pie(sorted_counts, labels = new_label, startangle = 90, counterclock = False);

# We have the used option `Square`. 
# Though, you can use either one specified here - https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axis.html?highlight=pyplot%20axis#matplotlib-pyplot-axis
plt.axis('square')
plt.title('Pokemon generation id Pie chart')
plt.show()

# Example 2. Plot a simple Donut plot
sorted_counts = pokemon['generation_id'].value_counts()

plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.5});
plt.axis('square')
plt.title('Pokemon generation id Donut chart')
plt.show()