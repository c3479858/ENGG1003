import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

#NEED TO RECHECK AND ADD COMMENTS BUT IT ALL SEEMS TO WORK
#HAVEN'T IMPLEMENTED EDGE CASE WHERE THE RESULT OF B IS NEGATIVE, CAN'T BE ASSED TBH

def f(x):                                                                           #Part A function
    return (x**2) * (np.sin(x)) + (2*x) - 3

def g(h, vTgt = 4, g = 9.81, L = 5):                                                #Part B function
    vClc = np.sqrt(2*g*h)*np.tanh((2/L)*np.sqrt(2*g*h))
    return vClc - vTgt

a1 = 0
b1 = 2
x = np.linspace(a1, b1, num=1000)                                                   #1000 points of x between 0 and 2
xBi, iters0 = rf.bisection(f, a1, b1)                                                                   #for graphing
xSe, iters1 = rf.secant(f, a1, b1)

a2 = 1
b2 = 10
h, iters2 = rf.secant(g, a2, b2)

print("a)\n   i) {:.5f} when subbed back into the eqn = {:.5f} (Bisection Method)".format(xBi, f(xBi)))
print("  ii) {:.5f} when subbed back into the eqn = {:.5f} (Secant Method)".format(xSe, f(xSe)))
print("b)    h = {:.2f}".format(h))

plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["f(x) = (x^2)sin(x) + 2x + 3"])
plt.title("Question 1a part i)")
plt.grid()
plt.show()