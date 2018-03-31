#!/usr/bin/python3
from module.maths import *
def g(x):
    return x ** 3 + 5 * (x ** 2)
print(newton_method(g, x = 1))
