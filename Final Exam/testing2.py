import numpy as np
from pandas.core.computation.common import result_type_many


def f(x):
    return (2 * x + 3)**2

def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    f_sum = 0
    i = 1
    while i < n:
        x = a + i*h
        f_sum += f(x)
        i += 1
    result = h*()
    return result
