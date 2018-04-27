"""
This is a custom module of functions that is created in order to practice algorithm and solve mathematics and statistics problems.
"""
def factorial(n):
    """
    Return n!.
    """
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)

def prime(n, factor=3):
    """
    Determine whether a number is prime or not.
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % factor == 0:
        return False
    if factor < n ** 0.5 and n % factor != 0:    
        return prime(n, factor + 2)
    return True

def choose(n, r):
    """
    The formula used in combination.
    """
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
    if n <= 1:
        return 0
    if n == 2:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result

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

def integral(f, start, end):
    """
    Using trapezoidal rule of integration to find the total area under a curve.
    """
    total_area = 0
    r = end - start
    num = int(r * 10000)
    width = r / num   # the width of trapezoidal.
    def y(n):
        """
        Return the list of y-cordinates.
        """
        result = []
        for i in range(n + 1):
            result.append(f(start + i * width))
        
        return result
    
    ycor = y(num)       
    for i in range(0, len(y(num)) - 1):
        a = (ycor[i] + ycor[i + 1]) * width / 2
        total_area += a
    return total_area

def normal(mean, var, start = None, end = None):
    from math import pi, e
    sd = var ** 0.5
    f = lambda x: 1 / ((2 * pi * (sd ** 2)) ** 0.5) * e ** (-((x - mean) ** 2) / (2 * (sd ** 2)))
    
    if start == None:
        start = mean - 5 * sd
    if end == None:
        end = mean + 5 * sd
    return round(integral(f, start, end), 5)

def root(n, lower = None, upper = None, deci = 4, power = 2):
    """
    Try to find the nth root for n using binary search.
    Square root by default.
    Correct to 4 decimal place by default.
    """
    if lower == None:
        lower = n

    if upper == None:
        upper = n

    if abs(lower - upper) <= 1 / (10 ** (deci * 2)):
        if lower ** power <= n:
            if upper ** 2 >= n:
                return (lower + upper) / 2

    if n < 0:
        return None

    mid = (lower + upper) / 2

    def decimal(x):
        return len(str(x).split('.')[1])

    def accu(x):
        if '.' in str(x):
            return 1 / (10 ** decimal(x))
        else:
            return 10 ** (len(str(x)) - 1)

    if upper ** power < n:
        return root(n, lower, upper + n / 8, deci, power)

    elif lower ** power > n:
        return root(n, lower - n / 8, upper, deci, power)

    elif abs(mid ** power - n) <= 1 / (10 ** deci):
        return round(mid, deci)

    elif mid ** power > n:
        return root(n, lower, mid - accu(mid), deci, power)

    elif mid ** power < n:
        return root(n, mid + accu(mid), upper, deci, power)

def differentiate(f, x, accu = 3):
    """
    Find the gradient of the curve f at the point (x, f(x))
    """
    step = 10 ** (-accu)
    return (f(x + step) - f(x)) / step

def newton_method(function, x=1):
    """
    Find one of the roots of equation f using Newton's method.
    f is the function of the equation.
    Correct to the 8th decimal place.
    Return False if can't find a root around the given value of x.
    """
    f = lambda x : eval(function)
    y = f(x)
    while abs(y) >= 10 ** (-14):
        m = differentiate(f, x)
        x = float(x) - y / m
        y1 = y
        y = f(x)
        if m == 0 and y > 10 ** (-14):
            return False
        if abs(y - y1) <= 10 ** (-14):
            break
    return round(x, 8)

def mean(array):
    """
    Calculate an estimated mean from mid-class values and thei frequencies.
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
