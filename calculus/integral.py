#!/usr/bin/python3
from math import *

"""
Changes have been applied so that the program runs to calculate pi.
If general numerical integration is needed, fix line 7, 65 and 67.
"""


def f(x):
    return sqrt(1 - x**2)


num = int(input("Enter the number of rectangle: "))
start_point = float(input("Enter the x cordinate of the start point: "))
end_point = float(input("Enter the x cordinate of the end point: "))
r = end_point - start_point  # range between the start and end point.


def mid_point():
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


def trapezoidal():
    """
    using trapezoidal rule of integration.
    """
    global num, start_point, end_point, r
    total_area = 0
    width = r / num  # the width of trapezoidal.

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


def main():
    choose = int(
        input(
            "which rule do you want to choose?\nMid-point(0) rule or trapezoidal(1) rule?: "
        )
    )
    if choose == 0:
        print(4 * mid_point())
    elif choose == 1:
        print(4 * trapezoidal())


main()
