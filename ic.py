'''
A file containing solutions for the entrance exam for Imperial College.
'''

def smaller_or_equal(n):
    if n <= 1:
        return 1
    else:
        return 2 * smaller_or_equal(int(n - 1 - 0.5)) + n


