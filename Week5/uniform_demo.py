import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.uniform(10, 20, size=N)
print(x)

plt.hist(x, bins=25)
plt.show()