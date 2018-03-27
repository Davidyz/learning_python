#!/usr/bin/python3
from module.maths import *
def g(x):
    return (x - 3) ** 2
print(newton_method(f = g))
