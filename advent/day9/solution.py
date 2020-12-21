def check_number(array, index, n=25):
    if index <= 24:
        return False
    preamble = array[index - n:index]
    for i in preamble:
        if (array[index] - i) in preamble:
            if (i * 2 == array[index] and preamble.count(i) >= 2) or (i * 2 != array[index]):
                return True
    return False

with open('input.txt') as fin:
    numbers = [int(i.replace('\n', '')) for i in fin.readlines()]

for i in range(25, len(numbers)):
    if not check_number(numbers, i):
        invalid_number = numbers[i]
        print(numbers[i])

for start in range(len(numbers) - 1):
    weakness = []
    for end in range(start + 1, len(numbers)):
        s = sum(numbers[start:end])
        if s < invalid_number:
            continue
        elif s == invalid_number:
            weakness = numbers[start:end]
            break
        elif s > invalid_number:
            break
    if weakness:
        break

print(min(weakness) + max(weakness))
