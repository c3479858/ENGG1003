import numpy as np
import matplotlib.pyplot as plt

N = 100000
# draw from range [10,20)
x = np.random.uniform(-5, 5, size=N)
print(x)

plt.hist(x, bins=20)
plt.show()