#def arctan(x):
#    for i in range(1, 23, 4):
#        x += (1/(i*x**i)) - (1/((3*i)*x**(3*i)))            #NEEDS DEBUGGING
#print(x)
#    return x

import numpy as np

def arctan(x):

    for i in range(1, 23, 4):
        x += 1/(i*(x**i))
    for i in range(3, 23, 4):
        x -= 1/(i*(x**i))
    return x
