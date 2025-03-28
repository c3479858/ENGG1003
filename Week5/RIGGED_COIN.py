import numpy as np

N = 100000
x = np.random.choice([0, 1], size=N, p=[0.6, 0.4])
headCnt = 0
for i in range(0, len(x)):
    if x[i] == 0:
        headCnt += 1

print(headCnt)