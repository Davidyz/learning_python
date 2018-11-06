#!/usr/bin/python3
from math import *
"""
A set of functions for numerical integration, giving the results as float.
You should always specify the number of intervals though it is unnecessary, because a fixed number of strips won't work efficiently. Eg, when the range is big, the number of strips should be increased as well, and vice versa (for less time and resource consumption).
"""

def xcor(n, start_point, r, num):
    """
    Return the x cordinate of the nth rectangle.
    For mid_point rule.
    """
    return start_point + 0.5 * (r / num) + (n - 1) * (r / num)

def area(f, n, start_point, r, num):
    """
    Return the area of the nth rectangle.
    For mid_point rule.
    """
    return f(xcor(n, start_point, r, num)) * (r / num)


def mid_point(f, start_point, end_point, num=10000):
    """
    Using the mid-point rule of integration.
    """
    r = end_point - start_point
    total_area = 0

    for i in range(1, int(num) + 1):
        total_area += area(f, i, start_point, r, num)
    
    return total_area

def y(f, n, start_point, width):
    """
    Return the list of y-cordinates.
    For trapezium rule.
    """
    result = []
    for i in range(int(n) + 1):
        result.append(f(start_point + i * width))
      
    return result
    
def trapezium(f, start_point, end_point, num=10000):
    """
    Using trapezoidal rule of integration.
    """
    r = end_point - start_point
    total_area = 0
    width = r / num   # the width of trapezoidal.

    ycor = y(f, num, start_point, width)       
    
    for i in range(len(ycor) - 1):
        a = (ycor[i] + ycor[i + 1]) * width / 2
        total_area += a

    return total_area

def simpson(f, start_point, end_point, num=10000):
    """
    Using simpson's rule to integrate.
    """
    if num % 2 == 0:
        return (2 * mid_point(f, start_point, end_point, num / 2) + trapezium(f, start_point, end_point, num / 2)) / 3
