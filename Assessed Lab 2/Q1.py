import numpy as np
import matplotlib.pyplot as plt

#PART A
def factNum(num):
    n = num
    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac

#PART C
def coshNum(x, n):
    cosh = 0
    while n>=0:
        cosh += (x**(2*n))/(factNum(2*n))
        n -= 1
    return cosh

#PART E (x array)
x = np.linspace(-5, 5, num=101)

#PART F (Computing z as a function of x)
z = coshNum(x, n = 5)

#PART B (Testing PART A)
print("The output for FactNum when num = 5 is: {}".format(factNum(5)))

#PART D (Testing PART C)
print("The output for coshNum when x = 2 and n = 5 is: {:.2f} (to 2 decimal places)".format(coshNum(x = 2, n = 5)))

#PART G (Always put the graphs last!!)
plt.plot(x, z, "k")
plt.title("Signal Analysis")
plt.legend(["z = coshNum(x, n=5)"])
plt.xlabel("x")
plt.ylabel("z")
plt.grid()
plt.axis([-6, 6, 0, 80])
plt.show()