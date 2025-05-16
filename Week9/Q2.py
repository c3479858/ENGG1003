import numpy as np
import rootfinding as rf

def f(x):
    return np.exp(x) - 3*x

xLO = 0
xHI = 1
x = rf.bisection(f, xLO, xHI)
print(x)
x0 = 1
x1 = 2
x = rf.secant(f, x0, x1)
print(x)