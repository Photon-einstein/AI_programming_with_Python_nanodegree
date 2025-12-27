import numpy as np

# Example: Create a Numpy array using the numpy.random.randint() function.
# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))
# We print X
print()
print('X = \n', X)
print()
# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# Example: Create a Numpy array of "Normal" distributed random numbers, using the numpy.random.normal() function.
# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
Y = np.random.normal(0, 0.1, size=(1000,1000))
# We print Y
print()
print('Y = \n', Y)
print()
# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)
print('The elements in Y have a mean of:', Y.mean())
print('The maximum value in Y is:', Y.max())
print('The minimum value in Y is:', Y.min())
print('Y has', (Y < 0).sum(), 'negative numbers')
print('Y has', (Y > 0).sum(), 'positive numbers')
