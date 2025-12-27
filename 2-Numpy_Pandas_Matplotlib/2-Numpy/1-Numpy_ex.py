## We create a 1D ndarray that contains only integers
import numpy as np


x = np.array([1, 2, 3, 4, 5])

## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

## We create a rank 1 ndarray that only contains strings
y = np.array(['Hello', 'World'])

## We print information about y
print('\ny = ', y)
print('y has dimensions:', y.shape)
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)

## We create a rank 1 ndarray from a Python list that contains integers and strings
z = np.array([1, 2, 'World'])

## We print information about z
print('\nz = ', z)
print('z has dimensions:', z.shape)
print('z is an object of type:', type(z))
print('The elements in z are of type:', z.dtype)

## We create a rank 1 ndarray that contains integers
a = np.array([1, 2, 3])

## We create a rank 1 ndarray that contains floats
b = np.array([1.0, 2.0, 3.0])

## We create a rank 1 ndarray that contains integers and floats
c = np.array([1, 2.5, 4])

## We print the dtype of each ndarray
print('\nThe elements in a are of type:', a.dtype)
print('The elements in b are of type:', b.dtype)
print('The elements in c are of type:', c.dtype)

## We create a rank 1 ndarray of floats but set the dtype to int64
d = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)
## We print the dtype d
print('d = ', d)
print('The elements in d are of type:', d.dtype)

## We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('\nY = \n', Y)
## We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# Example - Save the NumPy array to a File
## We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])
## We save x into the current directory as 
np.save('my_array', x)
## We load the saved array from our current directory into variable y
y = np.load('my_array.npy')
## We print y
print()
print('y = ', y)
## We print information about the ndarray we loaded
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)