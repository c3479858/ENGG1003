import numpy as np
import rootfinding as rf

def f(x):
    return 2*np.exp(-x) - np.sin(x)

def g(x):
    return np.exp(x) - x - 2

def h(x):
    return np.tan(x) - x - 1

aLO = 0
aHI = 3
bLO = 2
bHI = 5
cLO = 0
cHI = 4
dLO = 0.5
dHI = 1.5
print(rf.bisection(f, aLO, aHI))
print(rf.bisection(f, bLO, bHI))
print(rf.bisection(g, cLO, cHI))
print(rf.bisection(h, dLO, dHI))
print(rf.secant(f, aLO, aHI))
print(rf.secant(f, bLO, bHI))
print(rf.secant(g, cLO, cHI))
print(rf.secant(h, dLO, dHI))