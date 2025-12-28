# Create a 5 x 5 ndarray X with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the
# array and assign the result to Y.

import numpy as np

# TODO: replace None with appropriate code
# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1, 26).reshape(5, 5)

# TODO: replace None with appropriate code
# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 == 1]

### Notebook grading
X_solution = np.arange(1,26).reshape(5,5)
Y_solution= X_solution[X_solution % 2 != 0]

if type(X) != np.ndarray or type(Y) != np.ndarray:
    print("`X` and `Y` should both be ndarrays")
elif np.array_equal(X, X_solution) and np.array_equal(Y, Y_solution):
    print("Nice work! You can view my solution below")
elif X.shape != X_solution.shape:
    print("Your answer for `X` has a shape of {} but it should be 5 x 5".format(X.shape))
elif len(Y) != len(Y_solution):
    print("Your answer for `Y` has a length of {} but it should have a length of 13".format(len(Y)))
else:
    print("Your answers have the right shape but incorrect values")
