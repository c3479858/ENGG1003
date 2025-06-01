import numpy as  np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def line(t, m, b):
    return m * t + b

np.random.seed(3)

N = 11
t = np.linspace(0, 100, num=N)
n = np.random.uniform(-25, 25, N)

mm = 3
bb = 50
y = mm*t +bb + n

popt, _ = curve_fit(line, t, y)
m = popt[0]
b = popt[1]

ybest = m * t + b

plt.plot(t, y, "ro")
plt.plot(t, ybest, "b")
plt.show()