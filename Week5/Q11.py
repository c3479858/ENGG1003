#len(x) = N+2
N = 8
x = [0, 1]
for _ in range(N):
    x.append(x[-1] + x[-2])
print(x[0:N+2])