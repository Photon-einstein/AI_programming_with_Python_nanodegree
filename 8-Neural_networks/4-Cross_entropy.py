import numpy as np


def cross_entropy(Y, P):
    """
    This function takes as input two lists Y and P, and returns the float
    corresponding to their cross-entropy.
    """
    if len(Y) != len(P):
        return 0
    sum = 0.0
    for i in range(len(Y)):
        if Y[i] == 1:
            sum -= np.log(P[i])
        else:
            sum -= np.log(1 - P[i])
    return sum
