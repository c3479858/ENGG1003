import numpy as np
import matplotlib.pyplot as plt

N = 100000
x = np.random.normal(0, 10, size=N)

plt.hist(x, bins=200)
plt.show()