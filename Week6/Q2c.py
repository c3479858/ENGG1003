n = 6
x = []
y = (n*((2*n) + 1)*((2*n) - 1))/3
for i in range(1, 2*n, 2):
    x.append(i**2)

if sum(x) == y:
    print("Correct!")