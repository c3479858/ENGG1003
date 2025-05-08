import numpy as np

def myminmax(x):
    min = x[0]
    max = x[0]
    for i in range(0, len(x)):
        if x[i] > max:
            max = x[i]
        if x[i] < min:
            min = x[i]
    return int(min), int(max)

np.random.seed(1)
x = np.random.randint(-5, 5, size=10)

print(x)
print(myminmax(x))