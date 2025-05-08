import numpy as np

def areapoly(n, s = 1):
    return (1/4)*(n*s**2)*(1/np.tan(np.pi/n))

print(areapoly(n = 4))
