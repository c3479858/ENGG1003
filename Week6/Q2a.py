n = 6
x = []
y = (n * (n + 1) * (2 * n + 1)) / 6
for i in range(1, n+1, 1):
    x.append(i**2)                      #Don't need to use x = [] and x.append when you can just
                                        #make x = 0 and += onto x
if sum(x) == y:
    print("Correct!")