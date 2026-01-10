import numpy as np

# Example 2. Slicing and editing elements in a 2-D ndarray
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)
# We print X
print()
print("X = \n", X)
print()
# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 4th columns
Z = X[1:4, 2:5]
# We print Z
print()
print("Z = \n", Z)
print()
# We change the last element in Z to 555
Z[2, 2] = 555
# We print X
print()
print("X = \n", X)
print()
