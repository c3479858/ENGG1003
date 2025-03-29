#Part A
import numpy as np
np.random.seed(1)
x = np.random.randint(0, 101, size=35)
#Part B
markAvg = np.mean(x)                                            #Could be wrong, come back to this!!!
#Part C
markMax = "placeholder"
#Part D
markFail = "placeholder"
#Part E
markAdj = "placeholder"
#Part F
print("Students have the following marks:",x)
print("The average of marks is:{:.2f}".format(markAvg))
print("The max mark is:{}".format(markMax))
print("The number of elements less than 50 is:{}".format(markFail))
print("Here is the array after elements less than 25 being doubled:{}".format(markAdj))