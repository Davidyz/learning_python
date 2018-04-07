"""
This is a custom module of functions that is created in order to practice algorithm and solve mathematics and statistics problems.
"""
def factorial(n):
    """
    return n!.
    """
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)


def prime(n, factor=3):
    """
    determine whether a number is prime or not.
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
    the formula used in combination.
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

def febonacci(n):
    """
    Return the list of the first n numbers in the febonacci sequence.
    """
    return

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

def binomial(total, prob, suc):
    """
    prob = probability.
    suc = number of successful event.
    Calculate the probability for binomial distribution.
    """
    return choose(total, suc) * (prob ** suc) * ((1 - prob) ** (total - suc))

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

def newton_method(f, x=1):
    """
    Find one of the roots of equation f using Newton's method.
    f is the function of the equation.
    Correct to the 8th decimal place.
    """
    y = f(x)
    while abs(y) >= 10 ** (-14):
        m = differentiate(f, x)
        x = float(x) - y / m
        y1 = y
        y = f(x)
        if abs(y - y1) <= 10 ** (-14):
            break
    return round(x, 8)
