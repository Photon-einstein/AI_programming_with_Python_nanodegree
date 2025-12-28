import numpy as np

# Example 4 a. Use an array as indices to either make slices, select, or change elements
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1,3])

# We print X
print()
print('X = \n', X)
print()

# We print indices
print('indices = ', indices)
print()

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)

# Example 4 b. Use an array as indices to extract specific rows from a rank 2 ndarray.

# Let's create a rank 2 ndarray
X = np.random.randint(1,20, size=(50,5))
print("Shape of X is: ", X.shape)
print('X = \n', X)

# Create a rank 1 ndarray that contains a randomly chosen 10 values between `0` to `len(X)` (50)
# The row_indices would represent the indices of rows of X
row_indices = np.random.randint(0,50, size=10)
print("\nRandom 10 indices are: ", row_indices)

# To Do 1 - Print those rows of X whose indices are represented by entire row_indices ndarray
# Hint - Use the row_indices ndarray to select specified rows of X
X_subset = X[row_indices, :]
print('\nX subset_1= \n', X_subset)

# To Do 2 - Print those rows of X whose indices are present in row_indices[4:8]
X_subset = X[row_indices[4:8], :]
print('\nX subset_2= \n', X_subset)
