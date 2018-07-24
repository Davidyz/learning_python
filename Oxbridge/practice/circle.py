from math import pi
class Circle():
    '''
    A class for circle.
    '''
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * (self.radius ** 2)


