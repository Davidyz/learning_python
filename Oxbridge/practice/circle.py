from math import pi


class Circle:
    """
    A class for circle.
    Author: David
    Date: 25, 7, 2018.
    """

    def __init__(self, radius, xcor=0, ycor=0):
        self.r = radius
        self.x0 = xcor
        self.y0 = ycor

    def area(self):
        return pi * (self.r**2)

    def circumference(self):
        return 2 * pi * self.r
