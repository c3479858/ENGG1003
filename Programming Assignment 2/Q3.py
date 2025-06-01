import numpy as np                                                              #import numpy
import matplotlib.pyplot as plt                                                 #import pyplot
from scipy.interpolate import interp1d                                          #import interp fn
from scipy.optimize import curve_fit                                            #import curve fit
import pandas as pd                                                             #import pandas

def line(t, m, b):                                                              #line function for curve of best fit
    return m*t + b

#a)
#i)
t = np.linspace(0, 100, num=11)                                                 #given linspace
y = np.array([132, 138, 189, 229, 317, 304, 435, 435, 506, 545, 629])           #given array

plt.figure(1)                                                                   #for having multiple plots
plt.plot(t, y, "ro")                                                            #plots t vs y with red dots

#ii)
f = interp1d(t, y)                                                              #interpolates t vs y
yinterp = f(t)

plt.plot(t, yinterp, "b-")                                                      #plot t vs interpolated y

#iii)
t55 = 55                                                                        #what should I even call the fn? t55
y55 = f(t55)                                                                                            #feels wrong

#plt.plot(t55, y55, "go")                                                       #wasn't sure if "display" referred to
                                                                                #plotting it or just printing it
print("a)\n    iii) The interpolated value at t = 55 is {}".format(y55))        #I assumed printing

#b)
level = pd.read_csv("level.csv")

t = level["time (min)"].values                                                  #overwrote the earlier value of t
y = level["volume (L)"].values                                                  #overwrote the earlier value of y

curve, _ = curve_fit(line, t, y)

m = curve[0]                                                                    #extracting gradient from curve_fit
b = curve[1]                                                                    #extracting y intercept from curve_fit

ybest = m * t + b                                                               #plotting line of best fit
volume = 400                                                                    #given volume to find t
t400 = (volume - b) / m                                                         #rearranged line eqn

print("b)\n     ii) It will take {:.1f} minutes to fill the tank to {} Litres".format(t400, volume))

plt.figure(2)
plt.plot(t, y, "ro")
plt.plot(t, ybest, "b-")
plt.xlabel("time (min)")
plt.ylabel("volume (L)")
plt.title("Water Volume in a Filling Tank")

plt.show()                                                                      #shows both plot figures