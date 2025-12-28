import numpy as np

# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))
# We print x
print()
print('Original x = ', x)
# We sort x and print the sorted array using sort as a method.
x.sort()
# When we sort in place the original array is changed to the sorted array. To see this we print x again
print()
print('x after sorting:', x)
