import numpy as np

for i in range(10, 0, -1):
    print(i)
print("---")                            #use print("---") as a line break
for i in range(5, -6, -1):
    print(i)
print("---")
for i in range(10, -10, -2):
    print(i)

# Extra cool stuff:
# Printing as an array (horizontal)
print(np.array(range(10, 0, -1)))
# Another way as a list (horizontal)
print(list(range(10, 0, -1)))