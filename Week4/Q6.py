import numpy as np

x = np.linspace(10, 12, num=3)
y = np.copy(x)
#y = x

print(y)
y[0] = 2

print(y)
print(x)