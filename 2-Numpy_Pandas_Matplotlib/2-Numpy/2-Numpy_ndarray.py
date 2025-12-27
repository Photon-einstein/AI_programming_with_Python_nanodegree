# We create a 3 x 4 ndarray full of zeros. 
import numpy as np


X = np.zeros((3,4))
# We print X
print()
print('X = \n', X)
print()
# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# We create a 3 x 2 ndarray full of ones. 
Y = np.ones((3,2))
# We print Y
print()
print('Y = \n', Y)
print()
# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype) 

# We create a 2 x 3 ndarray full of fives. 
Z = np.full((2,3), 5) 
# We print Z
print()
print('Z = \n', Z)
print()
# We print information about Z
print('Z has dimensions:', Z.shape)
print('Z is an object of type:', type(Z))
print('The elements in Z are of type:', Z.dtype)

# We create a 5 x 5 Identity matrix. 
W = np.eye(5)
# We print W
print()
print('W = \n', W)
print()
# We print information about W
print('W has dimensions:', W.shape)
print('W is an object of type:', type(W))
print('The elements in W are of type:', W.dtype)

# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
A = np.diag([10,20,30,50])
# We print A
print()
print('A = \n', A)
print()

# We create a rank 1 ndarray that has sequential integers from 0 to 9
B = np.arange(10)
# We print the ndarray
print()
print('B = ', B)
print()
# We print information about the ndarray
print('B has dimensions:', B.shape)
print('B is an object of type:', type(B))
print('The elements in B are of type:', B.dtype)

# We create a rank 1 ndarray that has sequential integers from 4 to 9. 
C = np.arange(4,10)
# We print the ndarray
print()
print('C = ', C)
print()
# We print information about the ndarray
print('C has dimensions:', C.shape)
print('C is an object of type:', type(C))
print('The elements in C are of type:', C.dtype)

# Example: Create a Numpy array using arange(start_val, stop_val, step_size)
# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
D = np.arange(1,14,3)
# We print the ndarray
print()
print('D = ', D)
print()
# We print information about the ndarray
print('D has dimensions:', D.shape)
print('D is an object of type:', type(D))
print('The elements in D are of type:', D.dtype)

# Example: Create a Numpy array using linspace(start, stop, n), with stop inclusive.
# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
E = np.linspace(0,25,10)
# We print the ndarray
print()
print('E = \n', E)
print()
# We print information about the ndarray
print('E has dimensions:', E.shape)
print('E is an object of type:', type(E))
print('The elements in E are of type:', E.dtype)

# Example: Create a Numpy array using linspace(start, stop, n), with stop excluded.
# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
F = np.linspace(0,25,10, endpoint = False)
# We print the ndarray
print()
print('F = ', F)
print()
# We print information about the ndarray
print('F has dimensions:', F.shape)
print('F is an object of type:', type(F))
print('The elements in F are of type:', F.dtype)

# Example: Create a Numpy array by feeding the output of arange() function as an argument to the reshape() function.
# We create a rank 1 ndarray with sequential integers from 0 to 19
F = np.arange(20)
# We print F
print()
print('Original F = ', F)
print()
# We reshape F into a 4 x 5 ndarray 
F = np.reshape(F, (4,5))
# We print the reshaped F
print()
print('Reshaped F = \n', F)
print()
# We print information about the reshaped F
print('F has dimensions:', F.shape)
print('F is an object of type:', type(F))
print('The elements in F are of type:', F.dtype)

# Example: Create a Numpy array by calling the reshape() function from the output of arange() function.
# We create a a rank 1 ndarray with sequential integers from 0 to 19 and
# reshape it to a 4 x 5 array 
Y = np.arange(20).reshape(4, 5)
# We print Y
print()
print('Y = \n', Y)
print()
# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# Example 12. Create a rank 2 Numpy array by using the reshape() function.
# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50,
# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10, endpoint=False).reshape(5,2)
# We print X
print()
print('X = \n', X)
print()
# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

#Example 13. Create a Numpy array using the numpy.random.random() function.
# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
O = np.random.random((3,3))

# We print O
print()
print('O = \n', O)
print()

# We print information about O
print('O has dimensions:', O.shape)
print('O is an object of type:', type(O))
print('The elements in x are of type:', O.dtype)