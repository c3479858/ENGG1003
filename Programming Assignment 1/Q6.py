import numpy as np
dice = 2
N = 1000                                                    #amount of times 2 dice are rolled
k = [1, 2, 3, 4, 5, 6]                                      #all values for k

for i in k:
    counter = 0
    for _ in range(1, N + 1):
        die = np.random.randint(1, 7, size=dice)            #rolls 2 dice into an array
        if max(die) < i:                                    #checks if the max number in the array is less than k
            counter += 1                                    # since if the max is less than k, both dice must have face
                                                            # values less than k
    print("The estimated probability that {} rolled dice "
          "will each land on less than {} is {:.4f}"
          .format(dice, i, counter / N))