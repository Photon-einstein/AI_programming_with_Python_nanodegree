import pandas as pd
import numpy as np

# We create a Pandas Series that stores a grocery list of just fruits
fruits = pd.Series(
    data=[
        10,
        6,
        3,
    ],
    index=["apples", "oranges", "bananas"],
)

# We display the fruits Pandas Series
print(fruits)

# Example 1. Element-wise basic arithmetic operations
# We print fruits for reference
print("\nOriginal grocery list of fruits:\n ", fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print("\nfruits + 2:\n", fruits + 2)  # We add 2 to each item in fruits
print()
print("\nfruits - 2:\n", fruits - 2)  # We subtract 2 to each item in fruits
print()
print("\nfruits  *2:\n", fruits * 2)  # We multiply each item in fruits by 2
print()
print("\nfruits / 2:\n", fruits / 2)  # We divide each item in fruits by 2
print()

# Example 2. Use mathematical functions from NumPy to operate on Series

# We print fruits for reference
print("Original grocery list of fruits:\n", fruits)

# We apply different mathematical functions to all elements of fruits
print()
print("EXP(X) = \n", np.exp(fruits))
print()
print("SQRT(X) =\n", np.sqrt(fruits))
print()
print(
    "POW(X,2) =\n", np.power(fruits, 2)
)  # We raise all elements of fruits to the power of 2

# Example 3. Perform arithmetic operations on selected elements
# We print fruits for reference
print("\nOriginal grocery list of fruits:\n ", fruits)
print()

# We add 2 only to the bananas
print("Amount of bananas + 2 = ", fruits["bananas"] + 2)
print()

# We subtract 2 from apples
print("Amount of apples - 2 = ", fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print(
    "We double the amount of apples and oranges:\n", fruits[["apples", "oranges"]] * 2
)
print()

# We divide apples and oranges by 2
print(
    "We half the amount of apples and oranges:\n", fruits.loc[["apples", "oranges"]] / 2
)

# Example 4. Perform multiplication on a Series having integer and string elements
# We multiply our grocery list by 2
groceries = pd.Series(
    data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"]
)
print("\nDouble the groceries result:\n", groceries * 2)
