import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

def f(x):
    return (x**4) - 0.5*(x**3) - 100.5*(x**2) + (50*x) + 50

a = 0
b = 2
c = -1
d = 0

xBi, iters = rf.bisection(f, a, b)
xBi2, iters = rf.bisection(f, c, d)

x = np.linspace(-2, 2, num = 1001)

print("The root at [{}, {}] is {}, when computed back into f(x) we get {:.4f} (4d.p.)"
      .format(      a,   b,    xBi,                                    f(xBi)))
print("The root at [{}, {}] (from graph) is {}, when computed back into f(x) we get {:.4f} (4d.p.)"
      .format(      c,   d,                xBi2,                                    f(xBi2)))

plt.plot(x, f(x))
plt.title("Table 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()