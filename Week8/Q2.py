import numpy as np

def mult(x):
    y = x[0]
    for i in range(1, 5):
        y *= x[i]
    return y

x = np.array([8, 2, 3, -1, 7.5])
print(mult(x))
