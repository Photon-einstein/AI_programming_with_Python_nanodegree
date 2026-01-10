import numpy as np

# Example 5. Sort rank-2 arrays by specific axis.
# We create an unsorted rank 2 ndarray
X = np.random.randint(1, 11, size=(5, 5))
# We print X
print()
print("Original X = \n", X)
print()
# We sort the columns of X and print the sorted array
print()
print("X with sorted columns :\n", np.sort(X, axis=0))
# We sort the rows of X and print the sorted array
print()
print("X with sorted rows :\n", np.sort(X, axis=1))
