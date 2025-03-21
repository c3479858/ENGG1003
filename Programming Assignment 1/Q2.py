sum = []
for i in range(1, 61):
    if i % 5 == 0 or i % 3 == 0:
        sum.append(i)
print(sum)                              #Testing to make sure it's all stored in a list