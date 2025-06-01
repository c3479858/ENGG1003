import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

def f(x):                                                                           #Part A function
    return (x**2) * (np.sin(x)) + (2*x) - 3

#didn't implement  anything for the edge case where a2 is negative, which breaks the fn g(h), unless you feed it
#bad data though, it shouldn't affect it negatively ¯\_(ツ)_/¯

def g(h, vTgt = 4, g = 9.81, L = 5):                                                #Part B function
    vClc = np.sqrt(2*g*h)*np.tanh((2/L)*np.sqrt(2*g*h))
    return vClc - vTgt                                                              #f(h) - v = 0 hint used

a1 = 0                                                                              #part i interval
b1 = 2

x = np.linspace(a1, b1, num=1000)                                                   #1000 points of x between 0 and 2
                                                                                                        # for graphing
xBi, iters0 = rf.bisection(f, a1, b1)
xSe, iters1 = rf.secant(f, a1, b1)

a2 = 1                                                                              #part ii interval
b2 = 10
h, iters2 = rf.secant(g, a2, b2)                                                    #calculating h when v = 4m.s-1

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