import pandas as pd

# Example 1. Create a DataFrame
# We create a list of Python dictionaries
items2 = [
    {"bikes": 20, "pants": 30, "watches": 35, "shirts": 15, "shoes": 8, "suits": 45},
    {
        "watches": 10,
        "glasses": 50,
        "bikes": 15,
        "pants": 5,
        "shirts": 2,
        "shoes": 5,
        "suits": 7,
    },
    {"bikes": 20, "pants": 30, "watches": 35, "glasses": 4, "shoes": 10},
]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index=["store 1", "store 2", "store 3"])

# We display the DataFrame
print("\n", store_items)

# Example 2 a. Count the total NaN values
# We count the number of NaN values in store_items
x = store_items.isnull().sum().sum()

# We print x
print("\nNumber of NaN values in our DataFrame:", x)

# Example 2 b. Return boolean True/False for each element if it is a NaN
print("\n", store_items.isnull())

# Example 2 c. Count NaN down the column.
print("\n", store_items.isnull().sum())

# Example 3. Count the total non-NaN values
# We print the number of non-NaN values in our DataFrame
print(
    "\nNumber of non-NaN values in the columns of our DataFrame:\n", store_items.count()
)

# Example 4. Drop rows having NaN values
# We drop any rows with NaN values
print("\n", store_items.dropna(axis=0))

# Example 5. Drop columns having NaN values
# We drop any columns with NaN values
print("\n", store_items.dropna(axis=1))

# Example 6. Replace NaN with 0
# We replace all NaN values with 0
print("\n", store_items.fillna(0))

# Example 7. Forward fill NaN values down (axis=0) the dataframe
# We replace NaN values with the previous value in the column
print("\n", store_items.ffill(axis=0))

# Example 8. Forward fill NaN values across (axis=1) the dataframe
# We replace NaN values with the previous value in the row
print("\n", store_items.ffill(axis=1))

# Example 9. Backward fill NaN values down (axis=0) the dataframe
# We replace NaN values with the next value in the column
print("\n", store_items.bfill(axis=0))

# Example 10. Backward fill NaN values across (axis=1) the dataframe
# We replace NaN values with the next value in the row
print("\n", store_items.bfill(axis=1))

# Example 11. Interpolate (estimate) NaN values down (axis=0) the dataframe
# We replace NaN values by using linear interpolation using column values
print("\n", store_items.interpolate(method="linear", axis=0))

# Example 12. Interpolate (estimate) NaN values across (axis=1) the dataframe
# We replace NaN values by using linear interpolation using row values
print("\n", store_items.interpolate(method="linear", axis=1))
