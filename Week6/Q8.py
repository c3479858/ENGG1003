n = 19
n0 = n
i = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
    i += 1

print("{} iterations needed to reach 1 from {}".format(i, n0))