from math import *

"""
Using the middle rule of integration.
"""

def f(x):
    return x ** 2

num = int(input("Enter the number of rectangles: "))
start_point = float(input("Enter the x cordinate of the start point: "))
end_point = float(input("Enter the x cordinate of the end point: "))
r = end_point - start_point
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

print(total_area)
