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
    def __init__(self, sides):
        self.n = len(sides)
        self.sides = sides
    
    def input_sides(self, array):
        if len(array) == self.n:
            self.sides = array
        else:
            raise IndexError('Unmatched number of sides!')

    def display_side(self):
        for i in self.sides:
            print(i)

if __name__ == '__main__':

    b = B()

    try:
        b.printA()
        print(b.name)
    except Exception as er:
        print(er)

    b.printB()
    print(b.name2)
