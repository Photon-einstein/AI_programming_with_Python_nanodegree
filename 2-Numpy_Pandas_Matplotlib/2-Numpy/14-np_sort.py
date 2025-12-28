import numpy as np

# Example 3. Sort arrays using sort() function
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))
# We print x
print()
print('Original x = ', x)
# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))
# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)
