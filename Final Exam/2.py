def series(x, n):
    sum = 0
    for i in range(1, n+1):
        sum += (-1)**(i+1) * x**i / i
    return sum

print(series(3, 3))
