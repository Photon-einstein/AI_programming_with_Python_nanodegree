# We import Pandas as pd into Python
import pandas as pd

# We create a dictionary of Pandas Series
items = {
    "Alice": pd.Series(
        data=[40, 110, 500, 45], index=["book", "glasses", "bike", "pants"]
    ),
    "Bob": pd.Series(data=[245, 25, 55], index=["bike", "pants", "watch"]),
}

# We print the type of items to see that it is a dictionary
print(type(items))

# Example 1. Create a DataFrame using a dictionary of Series.
# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
print("\n", shopping_carts)

# Example 2. DataFrame assigns the numerical row indexes by default.
# We create a dictionary of Pandas Series without indexes
data = {"Alice": pd.Series([40, 110, 500, 45]), "Bob": pd.Series([245, 25, 55])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
print("\n", df)

# Example 3. Demonstrate a few attributes of DataFrame
# We print some information about shopping_carts
print("\nshopping_carts has shape:", shopping_carts.shape)
print("shopping_carts has dimension:", shopping_carts.ndim)
print("shopping_carts has a total of:", shopping_carts.size, "elements")
print()
print("The data in shopping_carts is:\n", shopping_carts.values)
print()
print("The row index in shopping_carts is:", shopping_carts.index)
print()
print("The column index in shopping_carts is:", shopping_carts.columns)

# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=["Bob"])

# We display bob_shopping_cart
print("\n", bob_shopping_cart)

# Example 4. Selecting specific rows of a DataFrame
# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index=["pants", "book"])

# We display sel_shopping_cart
print("\n", sel_shopping_cart)

# Example 5. Selecting specific columns of a DataFrame
# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(
    items, index=["glasses", "bike"], columns=["Alice"]
)

# We display alice_sel_shopping_cart
print("\n", alice_sel_shopping_cart)

# Example 6. Create a DataFrame using a dictionary of lists
# We create a dictionary of lists (arrays)
data = {"Floats": [4.5, 8.2, 9.6], "Integers": [1, 2, 3]}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
print("\n", df)

# Example 7. Create a DataFrame using a dictionary of lists, and custom row-indexes (labels)
# We create a dictionary of lists (arrays)
data = {"Floats": [4.5, 8.2, 9.6], "Integers": [1, 2, 3]}

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index=["label 1", "label 2", "label 3"])

# We display the DataFrame
print("\n", df)

# Example 8. Create a DataFrame using a of list of dictionaries
# We create a list of Python dictionaries
items2 = [
    {"bikes": 20, "pants": 30, "watches": 35},
    {"watches": 10, "glasses": 50, "bikes": 15, "pants": 5},
]

# We create a DataFrame
store_items = pd.DataFrame(items2)

# We display the DataFrame
print("\n", store_items)

# Example 9. Create a DataFrame using a of list of dictionaries, and custom row-indexes (labels)
# We create a list of Python dictionaries
items2 = [
    {"bikes": 20, "pants": 30, "watches": 35},
    {"watches": 10, "glasses": 50, "bikes": 15, "pants": 5},
]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index=["store 1", "store 2"])

# We display the DataFrame
print("\n", store_items)
