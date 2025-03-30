import numpy as np

N = 1000000
x = []
for i in range(1, N+1, 1):
    x.append(1/(i**2))

piAppr = np.sqrt(6*(sum(x)))

print("{:.10f} is {:.10f} away from pi at {} iterations".format(piAppr, (np.pi - piAppr), N))