#!/usr/bin/python3
from math import *
import maths
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

def LocalStationary(f, a, b, accu = 5):
    import random
    a, b = min(a, b), max(a, b)
    data = {}
    for i in range(int((b - a) // 10 ** (-accu))):
        x = random.uniform(a, b)
        y = f(x)
        data[x] = y

    maximum = (0, -inf)
    minimum = (0, inf)

    for i in data:
        if data[i] > maximum[1]:
            maximum = (i, data[i])
        if data[i] < minimum[1]:
            minimum = (i, data[i])

    return (round(minimum[1], accu), round(maximum[1], accu))

def MonteCarlo(f, a, b, accu=5):
    import random
    a, b = min(a, b), max(a, b)
    count_total = 0
    count_valid = 0
    r = LocalStationary(f, a, b, accu)
    if r[0] * r[1] >= 0:
        rect = abs(r[0] - r[1]) * (b - a)
        if r[1] <= 0:
            rect = -rect
    else:
        rect = abs(r[0] + r[1]) * (b - a)

    for i in range(int((b - a) // 10 ** (-accu))):
        x, y = random.uniform(a, b), random.uniform(r[0], r[1])
        count_total += 1
        if (y < f(x) and f(x) > 0) or (y > f(x) and f(x) <= 0):
            count_valid += 1

    return round(count_valid / count_total * rect, accu)
    
if __name__ == "__main__":
    def f(x):
        return e ** (- x ** 2 / 2)
    
    start_point = -100
    end_point = 100
    num = 500
    print("simpson  ", simpson(f, start_point, end_point, num))
    print("trapezium", trapezium(f, start_point, end_point, num))
    print("mid_point", mid_point(f, start_point, end_point, num))
