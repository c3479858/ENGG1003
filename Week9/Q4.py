import numpy as np
from fontTools.unicodedata import block

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
