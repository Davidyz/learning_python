#!/usr/bin/python3
from module.sort import *
import random
l = [1,2,3,4,5,6,7,8,9,10]
print(l)
print('=' * 50)
random.shuffle(l)
print(mergesort(l))
