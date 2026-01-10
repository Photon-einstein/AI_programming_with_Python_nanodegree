# We import Pandas as pd into Python
import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(
    data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"]
)

# We display the Groceries Pandas Series
print(groceries)

# We print some information about Groceries
print("\nGroceries has shape:", groceries.shape)
print("Groceries has dimension:", groceries.ndim)
print("Groceries has a total of", groceries.size, "elements")

# We print the index and data of Groceries
print("\nThe data in Groceries is:", groceries.values)
print("The index of Groceries is:", groceries.index)

# We check whether bananas is a food item (an index) in Groceries
x = "bananas" in groceries

# We check whether bread is a food item (an index) in Groceries
y = "bread" in groceries

# We print the results
print("\nIs bananas an index label in Groceries:", x)
print("Is bread an index label in Groceries:", y)

# We access elements in Groceries using index labels:

# We use a single index label
print("\nHow many eggs do we need to buy:", groceries["eggs"])
print()

# we can access multiple index labels
print("Do we need milk and bread:\n", groceries[["milk", "bread"]])
print()

# we use loc to access multiple index labels
print(
    "How many eggs and apples do we need to buy:\n", groceries.loc[["eggs", "apples"]]
)
print()

# Example 1. Access elements using index labels
# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print("\nHow many eggs and apples do we need to buy:\n", groceries.iloc[[0, 1]])
print()

# We use a negative numerical index
print("Do we need bread:\n", groceries.iloc[[-1]])
print()

# We use a single numerical index
print("How many eggs do we need to buy:", groceries.iloc[0])
print()
# we use iloc to access multiple numerical indices
print("Do we need milk and bread:\n", groceries.iloc[[2, 3]])

# Example 2. Mutate elements using index labels
# We display the original grocery list
print("\nOriginal Grocery List:\n", groceries)

# We change the number of eggs to 2
groceries["eggs"] = 2

# We display the changed grocery list
print()
print("Modified Grocery List:\n", groceries)

# Example 3. Delete elements out-of-place using drop()
# We display the original grocery list
print("Original Grocery List:\n", groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print("We remove apples (out of place):\n", groceries.drop("apples"))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print("Grocery List after removing apples out of place:\n", groceries)
