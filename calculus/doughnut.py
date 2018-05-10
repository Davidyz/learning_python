#!/usr/bin/python3
from math import *
"""
Try to compute the volume of a doughnut-shaped object. (a circle rotated around x-axis)
"""
radius = float(input('Enter the radius: '))
y_cor = float(input('Enter the y cordinate: '))

def f(x):
    global radius, y_cor
    return (sqrt(radius ** 2 - x ** 2) + y_cor) ** 2

def g(x):
    global radius, y_cor
    return (-sqrt(radius ** 2 - x ** 2) + y_cor) ** 2

num = 1000000 
start_point = -radius
end_point = radius
r = radius * 2            # range between the start and end point.

def mid_point(f):
    """
    Using the mid-point rule of integration.
    """
    global num, start_point, end_point, r
    total_area = 0
    def xcor(n):
        """
        return the x cordinate of the nth rectangle.
        """
        global start_point, end_point, r
        return start_point + 0.5 * (r / num) + (n - 1) * (r / num)

    def area(n):
        """
        return the area of the nth rectangle.
        """
        global start_point, end_point, r
        return f(xcor(n)) * (r / num)

    for i in range(1, num + 1):
        total_area += area(i)
    
    return total_area

if __name__ == '__main__':
    print(round(mid_point(f) - mid_point(g), 3), 'pi')
