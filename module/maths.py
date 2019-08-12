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

import math, cmath

pi = math.pi
e = math.e
cos = math.cos
sin = math.sin

def factorial(n):
    """
    Return n!.
    Return -1 if input is not valid (not a natural number).
    """
    if int(n) != n or n < 1:
        return -1

    i = 1
    result = 1
    while i <= n:
        result = result * i
        i += 1
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

def fibonacci(n):
    """
    Return the nth number in the fibonacci sequence.
    Starting from 0, 1
    """
    a, b = 0, 1
    while n > 1:
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

def mean(array):
    """
    Calculate an estimated mean from mid-class values and their frequencies.
    Input file should be an array containing sub arrays, and each subarray should have the value as the first item and its frequency as the second.
    """
    tx = 0
    tf = 0
    for i in array:
        tx += i[0] * i[1]
        tf += i[1]
    return tx / tf

def sd(array):
    """
    Calculate an estimated standard deviation from mid-class values and their frequencies.
    The input should has the same format as mean().
    """
    tx2f = 0
    tf = 0
    for i in array:
        tx2f += (i[0] ** 2) * i[1]
        tf += i[1]
    return (tx2f / tf - mean(array) ** 2) ** 0.5

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

if __name__ == '__main__':
    import sys
    print(newton_method(lambda x:math.cos(x) - x, lambda x:-math.sin(x) - 1, 100, 2))
