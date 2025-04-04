import time
import numpy as np

t0 = time.perf_counter()

N = 100000000
t = np.linspace(0, 1, num=N)
x = np.sin(t**2)
t1 = time.perf_counter()
print("Loop time (s): {:.2f}.".format(t1 - t0))