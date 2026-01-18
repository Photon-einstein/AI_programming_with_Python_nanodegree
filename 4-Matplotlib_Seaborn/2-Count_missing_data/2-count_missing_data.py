# Step 1. Load the dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Read the data from a CSV file
# Original source of data: https://www.kaggle.com/manjeetsingh/retaildataset available under C0 1.0 Universal (CC0 1.0) Public Domain Dedication License
sales_data = pd.read_csv('sales_data.csv')
print("Sales Data first 10 entries:\n", sales_data.head(10))
print("\nSales Data table shape: ", sales_data.shape)

# Use either of the functions below
# sales_data.isna()
print("\nSales Data table output:\n", sales_data.isnull())

print(sales_data.isna().sum())

# Step 2 - Prepare a NaN tabular data
# Let's drop the column that do not have any NaN/None values
na_counts = sales_data.drop(['Date', 'Temperature', 'Fuel_Price'], axis=1).isna().sum()
print("\nSales Data table output truncated:\n", na_counts)

# Step 3 - Plot the bar chart from the NaN tabular data, and also print values on each bar
# The first argument to the function below contains the x-values (column names), the second argument the y-values (our counts).
# Refer to the syntax and more example here - https://seaborn.pydata.org/generated/seaborn.barplot.html
sb.barplot(x=na_counts.index.values, y=na_counts)

# get the current tick locations and labels
plt.xticks(rotation=90) 

# Logic to print value on each bar
for i in range (na_counts.shape[0]):
    count = na_counts[i]

    # Refer here for details of the text() - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html
    plt.text(i, count+300, count, ha = 'center', va='top')

plt.title('NA bar plot')
plt.show()
