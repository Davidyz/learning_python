#!/usr/bin/python3
from math import *
"""
A set of functions for numerical integration, giving the results as float.
You should always specify the number of intervals though it is not necessary, because a fixed number of strips won't work efficiently. Eg, when the range is big, the number of strips should be increased as well, and vice versa (for less time and resource consumption).
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
    integral = 0
    interval = (end_point - start_point) / float(num)
    if num % 2 == 0:
        table = mapping(f, start_point, end_point, num)
        keys = tuple(i for i in table)
        for i in range(num + 1):
            if i % 2:
                integral += 4 * table[keys[i]]
            else:
                integral += 2 * table[keys[i]] 
        integral -= (table[keys[0]] + table[keys[-1]])
        return integral * interval / 3

    else:
        raise ValueError("num must be an even number!")

if __name__ == "__main__":
    def f(x):
        return e ** (- x ** 2 / 2)
    
    start_point = -1000
    end_point = 1000
    num = 10000
    print("simpson  ", simpson(f, start_point, end_point, num))
    print("trapezium", trapezium(f, start_point, end_point, num))
    print("mid_point", mid_point(f, start_point, end_point, num))
