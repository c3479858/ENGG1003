import numpy as np

#ARCTAN FUNCTION
def arctan(x):
    terms = 11
    output = 0
    for i in range(1, 2 * terms, 4):            #takes the numbers [1, 5, 9, 13, 17, 21]
        output += (1 / (i * x**i))              #adds 1/i*i^2 to the output
    for i in range(3, 2 * terms, 4):            #takes the numbers [3, 7, 11, 15, 19]
        output -= (1 / (i * x**i))              #subtracts 1/i*i^2 from the output
    return output

#TESTING CODE
pi = np.pi
piArc = 4 * (4 * arctan(5) - arctan(239))
if piArc - pi < 10**(-15):
    print("True")