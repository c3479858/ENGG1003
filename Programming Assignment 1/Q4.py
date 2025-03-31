#Part A
def numDigits(num):
    N = 0
    if num < 0:
        num = -num
    while num > 0:
        num //= 10
        N += 1
    return N

#Part B
def coPrime(n, m):
    if numDigits(n) == numDigits(m):
        return "True"
    else:
        return "False"

#Part C
x = [5678, 789, 1234]
y = [1234, -456, 0]
for i in range(0, 3, 1):
    print(coPrime(n=x[i], m=y[i]))