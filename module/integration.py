#!/usr/bin/python3
from math import *

def xcor(n):
    """
    Return the x cordinate of the nth rectangle.
    For mid_point rule.
    """
    return start_point + 0.5 * (r / num) + (n - 1) * (r / num)

def area(n):
    """
    Return the area of the nth rectangle.
    For mid_point rule.
    """
    return f(xcor(n)) * (r / num)


def mid_point(f, start_point, end_point, num=10000):
    """
    Using the mid-point rule of integration.
    """
    r = end_point - start_point
    total_area = 0

    for i in range(1, num + 1):
        total_area += area(i)
    
    return total_area

def y(n):
    """
    Return the list of y-cordinates.
    For trapezium rule.
    """
    result = []
    for i in range(n + 1):
        result.append(f(start_point + i * width))
      
    return result
    
def trapezium(f, start_point, end_point, num=10000):
    """
    Using trapezoidal rule of integration.
    """
    r = end_point - start_point
    total_area = 0
    width = r / num   # the width of trapezoidal.
    

    ycor = y(num)       
    
    for i in range(0, len(y(num)) - 1):
        a = (ycor[i] + ycor[i + 1]) * width / 2
        total_area += a

    return total_area

def simpson(f, start_point, end_point, num=10000):
    if num % 2 == 0:
        return (2 * mid_point(f, start_point, end_point, num / 2) + trapezium(f, start_point, end_point, num / 2)) / 3
