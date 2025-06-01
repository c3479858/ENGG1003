import numpy as np                                                                  #import numpy
import integration                                                                  #import integration.py from
                                                                                                            #directory
def f(x):                                                                           #i function
    return 7+(14*x**6)

def g(x):                                                                           #ii function
    return 2/(1+x**2)

def h(x):                                                                           #iii function
    return np.sqrt(x-x**2)

def i(x):                                                                           #part b function
    return np.e**((-x**2)/2)

np.random.seed(1)                                                                   #set seed as req.

fSim = integration.simpson(f, 0, 1, n = 100)                                        #integ i with 100 intervals
gSim = integration.simpson(g, 0, 1, n = 100)                                        #integ ii with 100 intervals
hSim = ((3 * np.sqrt(3)) / 4) + 24 * (integration.simpson(h, 0, 1/4, n = 600))      #integ iii with 600 intervals (req.)

a = -1                                                                              #a as req.
b =  3                                                                              #b as req.

iSim = (1/(np.sqrt(2*np.pi)))*(integration.simpson(i, a, b, n=1000))                #integ b with 1000 intevals as req.

N =  10**6                                                                          #N = 10^6 as req.
X = np.random.normal(0, 1, N)                                                       #random normal set

counter = 0
for i in X:                                                                         #counting how many values of X are
    if b >= i >= a:                                                                                 #between a and b
        counter += 1


#had a go at some fancy formatting for the answers, even shifted around the .format
#so that it each value lined up with its respective curly brackets

print("a)\n      i) {:.5f}\n     ii) {:.5f}\n    iii) {:.5f}"
      .format(       fSim,            gSim,            hSim))
print("b)\n      i) RHS of eqn = {:.3f}\n     ii) Percent of normal dist that fall within -1 and 3 = {:.3f}"
      .format(                    iSim,                                                            counter/N))