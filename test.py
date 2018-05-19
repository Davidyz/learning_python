#!/usr/bin/python3
from module.sort import *
from random import shuffle
l = []
for i in range(10):
    l.append(i)
shuffle(l)    
print(l)
print('=' * 30)
print(quicksort_s(l))
