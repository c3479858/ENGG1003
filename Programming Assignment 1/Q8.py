from math import factorial

length = 3                                                                      #amount of rows wanted

for n in range(length):                                                         #splitting length into individual rows
    for i in range(length-n+1):                                                 #left side spacing
        print(end=" ")

    for r in range(n+1):                                                        #setting up nCr eqn
        print(factorial(n) // (factorial(r) * factorial(n-r)), end=" ")         #nCr = n!/(r!*(n-r)!) and right spacing
    print()                                                                     #new row