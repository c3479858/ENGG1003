import numpy as np
#10 random integers from {0, 1}
# 0==heads 1==tails
N = 100
x = np.random.randint(0, 2, size=N)
#print(x)

headCnt = 0
for i in range(0, N):
    if x[i] == 0:
        headCnt += 1

print("Expected number of heads: {}".format(N/2))
print("Actual amount of heads: {}".format(headCnt))