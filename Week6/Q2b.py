n = 6
x = []
y = ((n**2)*((n + 1)**2))/4
for i in range(1, n+1, 1):
    x.append(i**3)

if sum(x) == y:
    print("Correct!")