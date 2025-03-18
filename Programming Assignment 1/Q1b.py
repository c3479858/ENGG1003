import numpy as np
import matplotlib.pyplot as plt
a = 1
b = -2
c =  -3
x = np.linspace(-5, 5, num=1001)        #list of 1001 values from -5 to 5

y = a*x**2 + b*x + c                         #equation
print("y =", y)                              #printing answers

plt.plot(x, y, "r")                    #plots the plot with a red line
plt.xlabel("x")
plt.ylabel("y", rotation=0)
plt.grid("on")                               #not sure why I have a warning here :/
plt.legend(["y = ax^2 + bx+ c"])
plt.show()                                   #displays the plot