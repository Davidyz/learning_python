#!/usr/bin/python3
from math import *
def mid_point(f, start_point, end_point, num=10000):
    """
    Using the mid-point rule of integration.
    """
    r = end_point - start_point
    total_area = 0

    def xcor(n):
        """
        return the x cordinate of the nth rectangle.
        """
        return start_point + 0.5 * (r / num) + (n - 1) * (r / num)

    def area(n):
        """
        return the area of the nth rectangle.
        """
        return f(xcor(n)) * (r / num)

    for i in range(1, num + 1):
        total_area += area(i)
    
    return total_area

def trapezium(f, start_point, end_point, num=10000):
    """
    using trapezoidal rule of integration.
    """
    r = end_point - start_point
    total_area = 0
    width = r / num   # the width of trapezoidal.
    
    def y(n):
        """
        return the list of y-cordinates.
        """
        result = []
        for i in range(n + 1):
            result.append(f(start_point + i * width))
        
        return result
    ycor = y(num)       
    
    for i in range(0, len(y(num)) - 1):
        a = (ycor[i] + ycor[i + 1]) * width / 2
        total_area += a

    return total_area

def simpson(f, start_point, end_point, num=10000):
    if num % 2 == 0:
        return (2 * mid_point(f, start_point, end_point, num / 2) + trapezium(f, start_point, end_point, num / 2)) / 3
