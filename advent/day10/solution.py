import math

def nth_bin(number, digit):
    return (number // (2 ** digit)) % 2

with open('input.txt') as fin:
    jolts = sorted([int(i.replace('\n', '')) for i in fin.readlines()])

target_jolts = max(jolts) + 3
differences = {1:0,
               2:0,
               3:0}

jolts_1 = [0] + jolts + [target_jolts]

for i in range(len(jolts_1) - 1):
    differences[jolts_1[i + 1] - jolts_1[i]] += 1

print(differences[1] * differences[3])

count2 = 0
def simplify(array, n, first_index = 1):
    if n == 0:
        return 0
    elif first_index == len(array) - 1:
        return False
    
    count = 0
    done = False
    for i in range(first_index, len(array) - 1):
        candidate = array.copy()
        if candidate[i + 1] - candidate[i - 1] <= 3:
            candidate.pop(i)
            done = True
            count += simplify(candidate, n - 1, first_index=i)
    return count

def search_2(array, index=1):
    count = 0
    for i in range(len(jolts_1) - 1):
        result = simplify(array.copy(), i)
        if result:
            count += result
        print(i, count)
    return count

print(search_2(jolts_1))
