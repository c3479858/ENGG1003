import numpy as np

#Part A
np.random.seed(1)
markAmount = 35
mark = np.random.randint(0, 101, size=markAmount)

#Part B
markSum = 0
for i in mark:
    markSum += i
markAvg = markSum/markAmount

#Part C
markMax = 0
for i in mark:
    if i > markMax:
        markMax = i

#Part D
markFail = 0
for i in mark:
    if i < 50:
        markFail += 1

#Part E
markAdj = np.copy(mark)
for i in range(0, markAmount, 1):
    if markAdj[i] < 25:
        markAdj[i] = 2*markAdj[i]

#Part F
print("Students have the following marks:",mark)                                                #Part A
print("The average of marks is: {:.3f}".format(markAvg))                                        #Part B
print("The max mark is: {}".format(markMax))                                                    #Part C
print("The number of elements less than 50 is: {}".format(markFail))                            #Part D
print("Here is the array after elements less than 25 being doubled: {}".format(markAdj))        #Part E