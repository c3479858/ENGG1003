import numpy as np

def f(x):
    return np.exp(x) - 3*x

eps = 1e-10
x0 = 0
x1 = 1
iters = 0
while abs(f(x1)) > eps:
    x = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
    x0 = x1
    x1 = x
    iters += 1

print("Soln: {}".format(x))
print("Iterations: {}".format(iters))
print("Check: f({:.8f}) = {:.6f}".format(x, f(x)))