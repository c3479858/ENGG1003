import numpy as np
import matplotlib.pyplot as plt

#Part A
a = 1
b = -2
c = -3
x = 4

y = a*x**2 + b*x + c                            #Formula
print("(Part A) y =", y)                        #Displaying the Answer

#Part B
x = np.linspace(-5, 5, num=1001)                #list of 1001 values from -5 to 5

y = a*x**2 + b*x + c                            #equation

plt.plot(x, y, "r")                             #plots the plot with a red line
plt.xlabel("x")
plt.ylabel("y", rotation=0)
plt.grid()
plt.legend(["y versus x"])
plt.title("Part B")
plt.show()                                      #displays the plot