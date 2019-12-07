"""
This is a custom module of functions that is created in order to practice algorithm and solve mathematics and statistics problems.
Currently support python3 only.
"""
from __future__ import division
import math, cmath, copy, random, integration

pi = math.pi
e = math.e
cos = math.cos
sin = math.sin
tan = math.tan
asin = math.asin
acos = math.acos
atan = math.atan
lg = math.log10

def ln(x):
    return math.log1p(x - 1)

def factorial(n):
    """
    Return n!.
    Return -1 if input is not valid (not a natural number).
    """
    if int(n) != n or n < 0:
        return -1

    if n <= 1:
        return 1

    result = 1
    while n >= 1:
        result *= n
        n -= 1
    
    return result

def isnumber(n):
    return isinstance(n, int) or isinstance(n, float)

def isprime(n):
    if isnumber(n):
        if n - int(n) != 0 or n <= 1:
            return -1

        if n == 2:
            return True
    
        elif n % 2 == 0:
            return False

        elif n % 2 != 0:
            factor = 3
            while True:
                if factor <= math.sqrt(n) + 1:
                    if n % factor == 0:
                        return False
                else:
                    break
                factor += 2
        return True
    else:
        return -1

def choose(n, r):
    """
    The formula used in combination.
    """
    if not (int(r) == r and int(n) == n):
        return -1
    if r > n:
        return -1
    if n == r:
        return 1
    elif r == 0:
        return 1
    
    res = factorial(n) / (factorial(r) * factorial(n - r))
    if int(res) == res:
        return int(res)
    else:
        return

def intpow(x, n):
    """
    Return the nth power of x.
    n has to be an integer.
    This method should work as long as n < 2 ** 1000, because Python has a maximum recursion depth of 1000.
    """
    if n % 1 != 0:
        return None
    elif n < 0:
        return 1 / intpow(x, -n)
    if n == 0:
        return 1
    elif n == 1:
        return x
    if n % 2 == 0:
        return intpow(x * x, n // 2)
    else:
        return intpow(x * x, (n - 1) // 2) * x

def fibonacci(n):
    """
    Return the nth number in the fibonacci sequence.
    Starting from 0, 1
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def binomial(n, p, start, end = None):
    """
    prob = probability.
    suc = number of successful event.
    Calculate the probability for binomial distribution.
    """
    if end == None:
        end = start
    result = 0
    while end >= start:
        result += choose(n, end) * (p ** end) * ((1 - p) ** (n - end))
        end -= 1
    return round(result, 10)

def normal(mean, var, start = None, end = None):
    from math import pi, e
    sd = var ** 0.5
    f = lambda x: 1 / ((2 * pi * (sd ** 2)) ** 0.5) * e ** (-((x - mean) ** 2) / (2 * (sd ** 2)))
    
    if end == None:
        end = start
        start = mean - 5 * sd
    return round(integration.simpson(f, start, end, 1000000), 5)

def root(m, power = 2):
    '''
    Try to find the nth(2 by default) root(+ve) for a real number m.
    '''
    f = lambda x:x ** power - m
    df = lambda x:power * (x ** (power - 1))
    x = 1
    y0 = 0
    y1 = f(x)
    while abs(y1 - y0) > 10 ** (-13):
        x = x - y1/df(x)
        y0 = y1
        y1 = f(x)
    return x

def differentiate(f, x, accu = 3):
    """
    Find the gradient of the curve f at the point (x, f(x))
    """
    step = 10 ** (-accu)
    return (f(x + step) - f(x)) / step

def newton_method(f, derivative = differentiate, x = 1, accuracy=14):
    """
    Find one of the roots of equation f using Newton's method.
    f is the function of the equation.
    Correct to the 8th decimal place.
    It is preferred to specify the derivative of f(x) as d(x). If not, a numerical method (differentiate(x)) will be used. It should work, but the result may be of low accuracy.
    Return False if can't find a root around the given value of x.
    """
    y = f(x)
    while abs(y) >= pow(10, -14):
        if derivative.__name__ == 'differentiate':
            m = derivative(f, x, accuracy)
        else:
            m = derivative(x)
        x = x - y / m
        y1 = y
        y = f(x)
        if abs(m) < pow(10, -14) and abs(y) > pow(10,0):
            return False
        if abs(y - y1) <= pow(10, -accuracy):
            return x
    return x

def summation(f, a, b=None):
    if b == None:
        b = a
        a = 1
    s = 0 
    for x in range(a, b + 1):
        s += f(x)
    return s

# Codes for statistics.
def mean(array):
    """
    Calculate an estimated mean from mid-class values and their frequencies.
    Input file should be an array containing sub arrays, and each subarray should have the value as the first item and its frequency as the second.
    """
    tx = 0
    tf = 0
    for i in array:
        if isinstance(i, list) or isinstance(i, tuple):
            tx += i[0] * i[1]
            tf += i[1]
        else:
            tx += i
            tf += 1
    return tx / tf

def moment(array, n=1):
    s = 0
    for i in array:
        if isinstance(i, list) or isinstance(i, tuple):
            s += i[1] * (i[0] ** n)
        else:
            s += i ** n
    return s

def StandardDeviation(array):
    return math.sqrt(moment(array, 2) - mean(array) ** 2)

# For complex number since here.

def arg(z):
    """
    Return the argument of a complex number.
    """
    if z.real == 0:
        if z.imag > 0:
            return pi / 2
        if z.imag < 0:
            return -pi / 2
        else:
            return 0
    angle = math.atan(float(z.imag) / z.real)
    if z.imag >= 0 and z.real < 0:
        angle += pi

    elif z.imag < 0 and z.real < 0:
        angle -= pi
    return angle

def modulus(z):
    """
    Return the modulus of a complex number.
    """
    return math.sqrt(pow(z.imag,2) + pow(z.real,2))

def cpow(z, n, polar = False):
    """
    Return the nth power of complex number z(Cartesian form by default).
    """
    angle = n * arg(z)
    mod = pow(modulus(z), n)
    while angle > pi:
        angle -= 2 * pi
    while angle <= -pi:
        angle += 2 * pi
    if polar == True:
        return (mod, angle)
    else:
        return mod * (cos(angle) + 1j * sin(angle))

# Codes for matrix. Temporarily without numpy.
class DimensionError(Exception):
   pass

class Vector():
    """
    Reinventing wheels to practice coding and make tools to cheat in maths homework.
    """
    def __init__(self, data):
        if isinstance(data, list):
            self.__vec = data
        elif isinstance(data, Matrix) and min(data.dimension()) == 1:
            if data.dimension()[1] >= data.dimension()[0]:
                self.__vec = data.row(0)
            else:
                self.__vec = data.column(0)
        else:
            raise ValueError('Please check the input. Only lists and matrix() are supported.')
    
    def __len__(self):
        return len(self.__vec)
    
    def __getitem__(self, n):
        return self.__vec[n]

    def __setitem__(self, index, value):
        self.__vec[index] = value

    def __add__(self, other):
        if len(self) == len(other):
            return [self[i] + other[i] for i in range(len(self))]

    def __abs__(self):
        return math.sqrt(sum([i ** 2 for i in self.__vec]))

    def __mod__(self, other):
        '''
        Return 1 if it is a zero vector divided by a zero vector.
        '''
        if isinstance(other, Matrix) and min(other.dimension()) == 1:
            return self % Vector(other)

        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] == other[i] == 0:
                    if i == len(self) - 1:
                        return 1
                else:
                    ratio = self[i] / other[i]
                    break
            
            for i in range(len(self)):
                if other[i] * ratio != self[i]:
                    return False
            return ratio
        return False

    def __eq__(self, other):
        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True

    def __mul__(self, other):
        if isnumber(other):
            new_vec = []
            for i in range(len(self)):
                new_vec.append(self[i] * other)
            return Vector(new_vec)
        
        if isinstance(other, Vector):
            if len(self) == len(other):
                return sum((self[i] * other[i] for i in range(len(self))))
    
    def normalised(self):
        '''
        Return the unit vector parallel to self.
        '''
        return self * (1 /abs(self))

    def show(self):
        print(self.__vec)

def angle(vec1, vec2):
    return acos(vec1 * vec2 / abs(vec1) / abs(vec2))

def CrossProduct(vec1, vec2):
    if len(vec1) == len(vec2) == 3: # only works for 3D vector now.
        return Vector([vec1[1] * vec2[2] - vec1[2] * vec2[1],
                       vec1[2] * vec2[0] - vec1[0] * vec2[2],
                       vec1[0] * vec2[1] - vec1[1] * vec2[0]])

class Matrix():
    """
    To assist maths homework and practice coding.
    """
    def __init__(self, mat, constant = False):
        for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i + 1]):
                raise ValueError('Not a valid matrix!')
        if constant:
            for i in range(len(mat)):
                mat[i] = tuple(mat[i])
            mat = tuple(mat)
            self.__const = True
        else:
            self.__const = False

        self.__mat = mat
        self.__dimension = [len(mat), len(mat[0])]
        self.__iterater = 0
        self.__CurrentRow = self.__mat[0]
        self.__columns = []
    
    def __eq__(self, other):
        if isinstance(other, Matrix) and other.dimension() == self.dimension():
            for i in range(self.dimension()[0]):
                for j in range(self.dimension()[1]):
                    if self.__mat[i][j] != other.row(i)[j]:
                        return False
            return True
        return False

    def __len__(self):
        return self.dimension()[0]

    def __abs__(self):
        return self.determinant()

    def __iter__(self):
        return iter(self.__mat)
    
    def __mul__(self, other):
        '''
        Self post-multiplied by other.
        '''
        if isinstance(other, Matrix):
            if self.dimension()[1] == other.dimension()[0]:
                result = [[0 for j in range(other.dimension()[1])] for i in range(self.dimension()[0])]
                row, column = len(result), len(result[0])

                for i in range(row):
                    for j in range(column):
                        result[i][j] = self[i] * other.column(j)
                return Matrix(result)

            else:
                raise DimensionError('The matrices are not conformable!')

        elif isnumber(other):
            newmat = copy.deepcopy(self.__mat)
            for i in range(self.dimension()[0]):
                for j in range(self.dimension()[1]):
                    newmat[i][j] *= other
            return Matrix(newmat)

        elif isinstance(other, Vector) and len(other) == self.dimension()[1]:
            other = Matrix([[i] for i in other])
            return self * other

    def __add__(self, n):
        if self.dimension() == n.dimension():
            newmat = []
            for i in range(self.dimension()[0]):
                newmat.append(list(Vector(self.__mat[i]) + Vector(n.row(i))))
            return Matrix(newmat)
        
        else:
            raise DimensionError('The matrices are not conformable!')
    
    def __sub__(self, other):
        return self + other * (-1)
    
    def __pow__(self, other):
        '''
        The recursive method works here and provides a higher efficiency than looping from 1 to n.
        '''
        if int(other) == other and self.dimension()[0] == self.dimension()[1]:
            return intpow(self, int(other))
        else:
            raise ValueError('Check your input! the power has to be int and the matrix has to be squaral.')

    def __neg__(self):
        return self * (-1)
    
    def __getitem__(self, x):
        return Vector(self.__mat[x])
    
    def __setitem__(self, x, y, value):
        if not self.__const:
            self.__mat[x][y] = value
        else:
            raise ValueError('This is a constant matrix!')
    
    def __mod__(self, other):
        if isinstance(other, Matrix) and self.dimension() == other.dimension():
            if not self[0] % other[0]:
                return False
            else:
                ratio = self[0] % other[0]

            for i in range(self.dimension()[0]):
                if other[i] * ratio != self[i]:
                    other[i].show()
                    self[i].show()
                    return False
            return ratio
        return False

    def isConst(self):
        return self.__const

    def minor(self, row, column):
        if self.dimension()[0] == self.dimension()[1]:
            min_matrix = copy.deepcopy(self.__mat)
            min_matrix.pop(row)
            for i in min_matrix:
                i.pop(column)

        return Matrix(min_matrix)
    
    def determinant(self):
        if self.__dimension[0] != self.__dimension[1]:
            raise DimensionError('This is not a square matrix and have no determinant.')
        if len(self) == 1:
            return self.row(0)[0]
        
        det = 0
        for i in range(self.__dimension[0]):
            det += self.__mat[0][i] * self.minor(0, i).determinant() * (-1) ** i
        
        return det
    
    def transpose(self):
        return Matrix(self.columns())

    def dimension(self):
        return [len(self.__mat), len(self.__mat[0])]

    def row(self, n):
        return self.__mat[n]

    def inverse(self):
        if self.__dimension[0] != self.__dimension[1]:
            raise DimensionError('This is not a square matrix and have no inverse.')

        det = self.determinant()
        if det == 0:
            return None
        else:

            inverse = [[0 for j in range(self.__dimension[0])] for i in range(self.__dimension[0])]
            for row in range(self.__dimension[0]):
                for column in range(self.__dimension[1]):
                    inverse[column][row] = self.minor(row, column).determinant() * (-1) ** (row + column) / det
            return Matrix(inverse)

    def column(self, n):
        return self.columns()[n]

    def columns(self):
        if self.__columns == []:
            for i in range(self.__dimension[1]):
                self.__columns.append(Vector([j[i] for j in self.__mat]))
        return self.__columns

    def show(self):
        for i in self.__mat:
            print(i)
        print('\n')

    def PopRow(self, n):
        if self.__dimension[0] > n:
            self.__dimension[0] -= 1
            return self.__mat.pop(n)

    def PopColumn(self, n):
        if self.dimension()[1] > n:
            self.dimension()[1] -= 1
            self.__columns = []
            return [i.pop(n) for i in self.__mat]
    
    def SetMinor(self, x, y, new_minor):
        '''
        Set the minor of the (x, y)th element to be the new_minor.
        '''
        new_minor = copy.deepcopy(list(new_minor))
        new_minor.insert(x, self.__mat[x])

        for i in range(self.dimension()[0]):
            if i != x:
                new_minor[i].insert(y, self.__mat[i][y])
        self.__mat = new_minor
        return self

    def InsertRow(self, row, n=None):
        if len(row) == self.dimension()[1]:
            new_mat = copy.deepcopy(self.__mat)

            if n == None:
                new_mat.append(list(row))
            else:
                new_mat.insert(n, list(row))
            return Matrix(new_mat)

        else:
            raise DimensionError('Matrix and row must have the same number of columns.')

    def InsertColumn(self, column, n=None):
        if len(column) == self.dimension()[0]:
            if n == None:
                n = self.dimension()[1] - 1

            new_mat = copy.deepcopy(self.__mat)
            for i in range(self.dimension()[0]):
                new_mat[i].append(column[i])
            return Matrix(new_mat)
        else:
            raise DimensionError('Matrix and column must have the same number of rows.')
    
    def SetRow(self, row, n):
        self.PopRow(n)
        self.InsertRow(row, n)

    def SetColumn(self, column, n):
        self.PopColumn(n)
        self.InsertColumn(column, n)
    
    def IsEigen(self, other):
        '''
        Check whether 'other' is an eigenvalue or eigenvector of self.
        If other is an eigenvector of self, the corresponding eigenvalue is returned.
        '''
        if isnumber(other):
            return (self - identity(self.dimension()[0]) * other).determinant() == 0
        elif isinstance(other, Vector) or isinstance(other, Matrix):
            return Vector(self * other) % other

def zeros(row, column):
    return Matrix([[0 for i in range(column)] for j in range(row)])

def identity(n):
    '''
    List comprehension was not fully applied because it appeaared to be much slower than an additional for loop.
    '''
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return Matrix(mat)

def randmat(row, column, bits=7, const=False):
    return Matrix([[random.getrandbits(bits) for i in range(column)] for j in range(row)], const)

def randvec(dim):
    return Vector(randmat(1, dim))

def rotate2(coordinates, angle):
    '''
    Rotate the coordinates anticlockwise by the angle measured in radian.
    '''
    return Matrix([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]) * coordinates

if __name__ == '__main__':
    import sys
    print(newton_method(lambda x:math.cos(x) - x, lambda x:-math.sin(x) - 1, 100, 2))
