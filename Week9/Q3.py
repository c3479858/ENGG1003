import numpy as  np
import rootfinding as rf

def f(x):
    return 3*x + np.sin(x) - np.exp(x)

xLO = -2
xHI = 4

x0 = 0
x1 = 1
x2 = 2
x = rf.bisection(f, x0, x1)
print(x)
x = rf.bisection(f, x1, x2)
print(x)
