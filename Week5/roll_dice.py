import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0, 7, size=10)
print(x)
plt.hist(x, bins=20)
plt.xlabel("Outcome of dice roll")
plt.ylabel("Number of outcomes")
plt.show()