import numpy as np


X = np.arange(0, 16, 1).reshape(4, 4)
print("X = \n", X)

Y = np.linspace(0, 16, 16, endpoint=False).reshape(4, 4)
print("Y = \n", Y)
