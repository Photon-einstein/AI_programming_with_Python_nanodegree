import numpy as np

# Example 1. Slicing in a 2-D ndarray
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)
# We print X
print()
print('X = \n', X)
print()
# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
# (The 1st being index 0)
Z = X[1:4,2:5]
# We print Z
print('Z = \n', Z)
# We can select the same elements as above using method 2
W = X[1:,2:]
# We print W
print()
print('W = \n', W)
# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]
# We print Y
print()
print('Y = \n', Y)
# We select all the elements in the 3rd row
v = X[2,:]
# We print v
print()
print('v = ', v)
# We select all the elements in the 3rd column
q = X[:,2]
# We print q
print()
print('q = ', q)
# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]
# We print R
print()
print('R = \n', R)
