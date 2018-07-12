def greatest_common_denominator(m, n):
    if n % (m % n) == 0:
        return m % n
    else:
        return greatest_common_denominator(n, m%n)
