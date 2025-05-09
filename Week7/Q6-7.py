#ROULETTE WHEEL
import numpy as np

N = 100
x = np.random.randint(0, 37, size=N)
wins = 0
spins = 0
spinsAvg = 0
for i in x:
    spins += 1
    if i == 0:
        wins += 1
        print("The house took {} spins to win!".format(spins))
        spinsAvg += spins
        spins = 0

print("The house won {} times! It took on average {} spins to win".format(wins, int(spinsAvg/wins)))