import numpy as np
import integration as integ

#NEED TO ADD COMMENTS AND CHECK CODE IS RIGHT BUT IT RUNS AND PRODUCES CORRECT RESULTS ¯\_(ツ)_/¯

def f(x):
    return 7+(14*x**6)
def g(x):
    return 2/(1+x**2)
def h(x):
    return np.sqrt(x-x**2)
def i(x):
    return np.e**((-x**2)/2)

np.random.seed(1)

fSim = integ.simpson(f, 0, 1, n = 100)
gSim = integ.simpson(g, 0, 1, n = 100)
hSim = ((3 * np.sqrt(3)) / 4) + 24 * (integ.simpson(h, 0, 1/4, n = 600))

a = -1
b =  3
iSim = (1/(np.sqrt(2*np.pi)))*(integ.simpson(i, a, b, n=1000))

N =  10**6
X = np.random.normal(0, 1, N)
counter = 0
for i in X:
    if b >= i >= a:
        counter += 1

print("a)\n      i) {:.5f}\n     ii) {:.5f}\n    iii) {:.5f}"
      .format(       fSim,            gSim,            hSim))
print("b)\n      i) RHS of eqn = {:.3f}\n     ii) Percent of normal dist that fall within -1 and 3 = {:.3f}"
      .format(                    iSim,                                                            counter/N))