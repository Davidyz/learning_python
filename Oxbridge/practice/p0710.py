def GreatestCommonDenominator(m, n):
    if n % (m % n) == 0:
        return m % n
    else:
        return GreatestCommonDenominator(n, m%n)
