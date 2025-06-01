import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#ADD COMMENTS THEN SUBMIT
#i)
t = np.linspace(0, 100, num=11)
y = np.array([132, 138, 189, 229, 317, 304, 435, 435, 506, 545, 629])
plt.plot(t, y, "ro")

#ii)
f = interp1d(t, y)
yInterp = f(t)
plt.plot(t, yInterp, "b-")

#iii)
t55 = 55
y55 = f(t55)
#plt.plot(t55, y55, "go")
print("The interpolated value at t = 55 is {}".format(y55))
plt.show()