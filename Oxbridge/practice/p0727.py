import math, itertools, sys
class A():
    def __init__(self):
        self.name = 'A'
    
    def printA(self):
        print('A1')

class B(A):
    def __init__(self):
        #A.__init__(self)
        self.name2 = 'B'
    
    def printB(self):
        print('B1')

class Polygon():
    '''
    Author: Davidyz;
    Date: 27, 7, 2018
    '''
    def __init__(self, num_of_sides):
        self.n = num_of_sides

        self.sides = list(0 for i in range(num_of_sides))
    
    def input_sides(self, array):
        if len(array) == self.n:
            self.sides = array
        else:
            raise IndexError('Unmatched number of sides!')

    def display_side(self):
        for i in range(len(self.sides)):
            print('Side{}: {}'.format(i + 1, self.sides[i]))

def valid_triangle(array):
    array.sort()
    return not sum(array[:2]) <= array[2]

class Triangle(Polygon):
    '''
    Author: Davidyz;
    Date: 27, 7, 2018
    '''
    def __init__(self, length):
        Polygon.__init__(self, 3)
        if valid_triangle(length):
            self.sides = length
        else:
            raise ValueError('Invalid lengths for a triangle!')

    def area(self):
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

if __name__ == '__main__':
    length = [float(i) for i in sys.argv[1:]]
    t1 = Triangle(length)
    t1.display_side()
    print(t1.area())
