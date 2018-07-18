#!/usr/bin/python3
from module import maths
import math
right_pole = 0
middle_point = [0, 20]
dx = 0.00001
coefficient = 0.0535521
length_of_string = 40.0
height_of_pole = 50
estimated_length = 0

def function(x):
    global coefficient
    return coefficient * (x ** 2) + 20

def rev_function(x):
    global coefficient
    return math.sqrt((x - 20) / coefficient)

def generate_dy():
    global coefficient, dx
    x = 0
    y = 20
    result = []
    while y <= 50:
        result.append(2 * coefficient * x * dx)
        x += dx
        y = function(x)
    return result

def find_the_sum_of_slope(list_of_dy):
    global dx
    return (sum(list(((i**2 + dx**2)**0.5) for i in generate_dy())))

def size_of_step(current_y):
    global length_of_string
    return math.sqrt(abs(length_of_string - current_y))

while abs(estimated_length - (length_of_string)) > 0.000001:
    if estimated_length > length_of_string:
        coefficient += 0.000000001 #size_of_step(estimated_length)
    else:
        coefficient -= 0.000000001 #size_of_step(estimated_length)
    estimated_length = find_the_sum_of_slope(generate_dy())
    
    print('working, coefficient = {}, estimated length = {}'.format(coefficient, round(estimated_length, 7)))

if abs(estimated_length - length_of_string / 2) < 0.01:
    print('The estimated length is {}, the coefficient is {}, the distance between poles is {}.'.format(estimated_length * 2, coefficient, 2 * rev_function(50)))
