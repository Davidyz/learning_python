#!/usr/bin/python3
from math import *
"""
A set of functions for numerical integration, giving the results as float.
You should always specify the number of intervals though it is unnecessary, because a fixed number of strips won't work efficiently. Eg, when the range is big, the number of strips should be increased as well, and vice versa (for less time and resource consumption).
"""

def mapping(f, start_point, end_point, num):
    """
    Map the function into a dictionary.
    """
    res = {start_point:f(start_point)}
    interval = (end_point - start_point) / float(num)

    for i in range(int(num) + 1):
        res[start_point + interval * i] = f(start_point + i * interval)
    
    return res

def mid_point(f, start_point, end_point, num=10000, table = None):
    """
    Using the mid-point rule of integration.
    Re-written with mapping().
    """
    total_area = 0
    interval = (end_point - start_point) / float(num)

    if table == None:
        critical_values = mapping(f, start_point + interval / 2, end_point - interval / 2, num - 1)
    else:
        critical_values = table
    index = tuple(critical_values.keys())

    for i in range(len(index)):
        total_area += interval * critical_values[index[i]]

    return total_area

def trapezium(f, start_point, end_point, num=10000, table = None):
    """
    Using trapezoidal rule of integration.
    Re-written with mapping().
    """
    total_area = 0
    interval = (end_point - start_point) / float(num)
    
    if table == None:
        critical_values = mapping(f, start_point, end_point, num)
    else:
        critical_values = table
    index = tuple(critical_values.keys())

    for i in range(len(index)):
        total_area += 2 * critical_values[index[i]]

    total_area -= (critical_values[index[0]] + critical_values[index[-1]])
    total_area = total_area * interval / 2

    return total_area

def simpson(f, start_point, end_point, num=10000):
    """
    Using simpson's rule to integrate.
    Re-written with mapping().
    """
    if num % 2 == 0:
        num = num // 2
        table = mapping(f, start_point, end_point, num)
        return (2 * mid_point(f, start_point, end_point, num, table) + trapezium(f, start_point, end_point, num, table)) / 3
    else:
        raise ValueError("num must be an even number!")

if __name__ == "__main__":
    def f(x):
        return sqrt(x ** 2 - 1)
    
    start_point = 1
    end_point = 2
    num = 100000
    print("simpson  ", simpson(f, start_point, end_point, num))
    print("trapezium", trapezium(f, start_point, end_point, num))
    print("mid_point", mid_point(f, start_point, end_point, num))
