import matplotlib.pyplot as plt
import numpy as np

current = []
time = []

for i in range(0, 41):
    time.append(i)
    current.append(np.e**((-1/5)*i)+0.02)

plt.plot(time, current, "k-.")
plt.axis([0, 40, 0.0, 1.2])
plt.legend(["capacitor charging current"])
plt.grid()
plt.title("RC Charging Circuit Curves")
plt.xlabel("Time Constant")
plt.ylabel("Capacitor Current")
plt.show()