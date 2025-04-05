import numpy as np

def polyarea(x, y):
    x1 = 0                                                  #first half of the eqn
    y1 = 0                                                  #second half
    n  = int((len(x) + len(y)) / 2)                         #making sure the lengths of both arrays are the same
    for i in range(0, n):
        x1 += x[i - 1] * y[i]                               #summing together all x(n-1)y(n) values for the arrays
        y1 += y[i - 1] * x[i]                               #same thing but for   y(n-1)x(n)
    return 1 / 2 * (np.abs(x1 - y1))                        #returns 1/2 the absolute value of x1 - y1

xcoord = np.array([1, 3, 4, 3.5, 2])                        #x coordinates array
ycoord = np.array([1, 1.2, 2.5, 5, 4])                      #y coordinates array

print("The area of the polygon is {:.3f} units squared"     #printing with context
      .format(polyarea(x = xcoord, y = ycoord)))