import numpy as np
np.random.seed(1)

def minpos(x):
    minx = x[0]
    mindex = 0
    for i in x:
        if i >= 0 < minx:
            minx = i

    return minx

x = np.random.normal(0, 1, size=10)
#mp, idx = minpos(x)
print(x)
print(minpos(x))
#print(mp)
#print(idx)

#WORK IN PROGRESS