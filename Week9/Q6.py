import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

def f(x):
    return np.exp(x) - 3*x**2

#PART B
x0 = -1
x1 = 0
x2 = 1
x3 = 3
x4 = 4
print(rf.bisection(f, x0, x1))
print(rf.bisection(f, x1, x2))
print(rf.bisection(f, x3, x4))

#PART A
x = np.linspace(-1, 5, num = 1000)
plt.plot(x, f(x))
plt.grid()
plt.show()

