import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

total = 0
count = 0
for i in range(0, len(m)):
    for r in range(0, len(m[0])):
        total += m[i, r]
        count += 1
avg = total/count
print(avg)

print(np.average(m))