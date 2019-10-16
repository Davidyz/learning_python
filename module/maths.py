"""
This is a custom module of functions that is created in order to practice algorithm and solve mathematics and statistics problems.
Currently support python3 only.
"""
from __future__ import division
try:
    from module import integration
except Exception:
    import sys
    sys.path.append('module/')
    import integration

import math, cmath, copy, random

pi = math.pi
e = math.e
cos = math.cos
sin = math.sin
tan = math.tan
asin = math.asin
acos = math.acos
atan = math.atan2
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

    if n < 0:
        return 1

    result = 1
    while n >= 1:
        result *= n
        n -= 1
    
    return result

def isprime(n):
    if isinstance(n, int) or isinstance(n, float):
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

def triangle(n):
    def triangle_helper(n, result = [1, [1, 1]]):
        if n == 2:
            return result
        elif n == 1:
            return 1
        else:
            temp = [1, 1]
            for i in range(len(result[-1]) - 1):
                temp.insert(-1, result[-1][i] + result[-1][i + 1])
            result.append(temp)
            return triangle_helper(n - 1, result)
    return triangle_helper(n)

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
        print(x)
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

def moment(array, n):
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

def VectorSum(vec1, vec2):
    if len(vec1) == len(vec2):
        return [vec1[i] + vec2[i] for i in range(len(vec1))]
    else:
        raise DimensionError('The vectors are not of the same dimension.')

def DotProduct(vect1, vect2):
    if len(vect1) == len(vect2):
        return sum((vect1[i] * vect2[i] for i in range(len(vect1))))
    else:
        raise ValueError('Vect1 and Vect2 are not with same dimensions.')

class matrix():
    def __init__(self, mat):
        for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i + 1]):
                raise ValueError('Not a valid matrix!')

        self.__mat = mat
        self.__dimension = len(mat), len(mat[0])
        self.__iterater = 0
        self.__CurrentRow = self.__mat[0]
    
    def __len__(self):
        return self.__dimension[0] * self.__dimension[1]

    def __iter__(self):
        return iter(self.__mat)

    def __mul__(self, other):
        '''
        Self post-multiplied by other.
        '''
        if isinstance(other, matrix):
            if self.__dimension[1] == other.dimension()[0]:
                result = [[0 for j in range(other.dimension()[1])] for i in range(self.__dimension[0])]
                row, column = len(result), len(result[0])

                for i in range(row):
                    for j in range(column):
                        result[i][j] = DotProduct(self.__mat[i], other.column(j))
                return result

            else:
                raise DimensionError('The matrices are not conformable!')

        elif isinstance(other, int) or isinstance(other, float):
            newmat = copy.deepcopy(self)
            for i in newmat:
                for j in i:
                    j = other * j
            return newmat

    def __add__(self, n):
        if self.__dimension == n.dimension():
            newmat = []
            for i in range(self.__dimension[0]):
                newmat.append(VectorSum(self.__mat[i], n.row(i)))
            return matrix(newmat)
        
        else:
            raise DimensionError('The matrices are not conformable!')
    
    def minor(self, row, column):
        if self.__dimension[0] == self.__dimension[1]:
            min_matrix = []
            for i in range(self.__dimension[0]):
                if i != row:
                    min_matrix.append(self.row(i))
                    min_matrix[-1].pop(column)
                
        return matrix(min_matrix)
    
    def determinant(self):
        if len(self) == 1:
            return self.row(0)[0]
        
        det = 0
        for i in range(self.__dimension[1]):
            det += self.__mat[0][i] * self.minor(0, i).determinant() * (-1) ** i
        
        return det

    def dimension(self):
        return self.__dimension

    def row(self, n):
        return self.__mat[n]

    def column(self, n):
        return [i[n] for i in self.__mat]

    def show(self):
        for i in self.__mat:
            print(i)
        print('\n')

def identity(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return matrix(mat)

def randmat(row, column, np=False):
    if np:
        import numpy
        return numpy.matrix([[random.getrandbits(7) for i in range(column)] for j in range(row)])
    else:
        return matrix([[random.getrandbits(7) for i in range(column)] for j in range(row)])

def add(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError('Mat1 and Mat2 are not of the same dimensions.')
    return [[mat1[row][column] + mat2[row][column] for column in range(len(mat1[0]))] for row in range(len(mat1))]

def transpose(matrix):
    transposed = [[] for i in range(len(matrix[0]))]

    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            transposed[column].append(matrix[row][column])

    return transposed

def minor(matrix, row, column):
    matrix = copy.deepcopy(matrix)
    min_matrix = []

    for i in range(len(matrix)):
        if i != row:
            min_matrix.append(matrix[i])
            min_matrix[-1].pop(column)
        else:
            pass

    return min_matrix

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError('Not a square matrix!')

    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            continue
        det += matrix[0][i] * determinant(minor(matrix, 0, i)) * (-1) ** i

    return det

def inverse(matrix):
    det = determinant(matrix)
    if len(matrix) != len(matrix[0]) or det == 0:
        return None
    
    matrix = copy.deepcopy(matrix)
    inverse = [[] for i in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            inverse[row].append((-1) ** (row + column) * determinant(minor(matrix, row, column)) / det)
    
    return transpose(inverse)

if __name__ == '__main__':
    import sys
    print(newton_method(lambda x:math.cos(x) - x, lambda x:-math.sin(x) - 1, 100, 2))
