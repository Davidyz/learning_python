# Q1
import maths, Array

a = Array.reversed([i for i in str(maths.factorial(2019))])
count = 0
for i in a:
    if i == "0":
        count += 1
    else:
        break
print("1. ", count)

# Q2
import itertools

numbers = (i for i in range(1, 2020))
pairs = (i for i in itertools.combinations(numbers, 2))
max_frac = (0, 1)
for i in pairs:
    frac = i[0] / i[1]
    if (frac < 7 / 11) and frac > max_frac[0] / max_frac[1]:
        max_frac = i
print("2. ", max_frac, "error: ", max_frac[0] / max_frac[1] - 7 / 11)
