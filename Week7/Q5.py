import numpy as np
import matplotlib.pyplot as plt

N = 100000
x = np.random.normal(loc=0, scale=2, size=N)
# bell curve for large N
plt.hist(x, bins=100)
plt.xlabel('Value of random number')
plt.ylabel('Number of samples in bin')
plt.show()