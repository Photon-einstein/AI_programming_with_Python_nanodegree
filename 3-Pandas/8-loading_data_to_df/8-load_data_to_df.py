import pandas as pd

# Example 1. Load the data from a .csv file.
# We load Google stock data in a DataFrame
google_stock = pd.read_csv('./GOOG.csv')

# We print some information about google_stock
print('google_stock is of type:', type(google_stock))
print('google_stock has shape:', google_stock.shape)

# Example 2. Look at the first few rows of the DataFrame
print("\nGoogle stock data:\n", google_stock)

# Example 3. Look at the first 5 rows of the DataFrame
print("\nGoogle stock data, first 5 rows:\n", google_stock.head())

# Example 4. Look at the last 5 rows of the DataFrame
print("\nGoogle stock data, last 5 rows:\n", google_stock.tail())

# Example 5. Check if any column contains a NaN. Returns a boolean for each column label.
print("\nCheck if any column contains a NaN:\n", google_stock.isnull().any())

# Example 6. See the descriptive statistics of the DataFrame
# We get descriptive statistics on our stock data
print("\nDescriptive statistics on our stock data:\n", google_stock.describe())

# Example 7. See the descriptive statistics of one of the columns of the DataFrame
# We get descriptive statistics on a single column of our DataFrame
print("\nDescriptive statistics on a single column of our DataFrame:\n", google_stock['Adj Close'].describe())

# Example 8. Statistical operations - Min, Max, and Mean
# We print information about our DataFrame  
print()
print('Maximum values of each column:\n', google_stock.max())
print()
print('Minimum Close value:', google_stock['Close'].min())
print()
print('Average value of each column:\n', google_stock.mean(numeric_only=True))

# Example 9. Statistical operation - Correlation
# We display the correlation between columns
print('\nCorrelation between columns:\n', google_stock.corr(numeric_only=True))

# We load fake Company data in a DataFrame
data = pd.read_csv('./fake_company.csv')

print("\nData from fake company:\n", data)

# We display the total amount of money spent in salaries each year
print("\nTotal amount of money spent in salaries each year", data.groupby(['Year'])['Salary'].sum())

# We display the average salary per year
print("\nAverage salary per year", data.groupby(['Year'])['Salary'].mean())

# Example 12. Demonstrate groupby() on single column
# We display the total salary each employee received in all the years they worked for the company
print("\nTotal salary each employee received in all the years they worked for the company", data.groupby(['Name'])['Salary'].sum())

# Example 13. Demonstrate groupby() on two columns
# We display the salary distribution per department per year.
print("\nSalary distribution per department per year", data.groupby(['Year', 'Department'])['Salary'].sum())
