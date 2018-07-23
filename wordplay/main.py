import itertools, sys

fin = open('wordplay/wordlist.txt', 'r')
wordlist = fin.readlines()
fin.close()
wordlist = list(i[:-1].lower() for i in wordlist)
letters = str(sys.argv[-1]).lower()
permutation = []
results = []

def join(array):
    string = ''
    for i in array:
        string += str(i)
    return string

def binary_search(word, array, start=0, end=None):
    if end == None:
        end = len(array) - 1
    if start == end:
        if word == array[start]:
            return start
        else:
            return None
    if start < end:
        middle = (start + end) // 2
        if word == array[middle]:
            return middle
        elif word > array[middle]:
            return binary_search(word, array, middle + 1, end)
        elif word < array[middle]:
            return binary_search(word, array, start, middle - 1)

for i in range(1, len(letters) + 1):
    permutation += list(itertools.permutations(letters, i))

for i in range(len(permutation)):
    permutation[i] = join(permutation[i])

for i in permutation:
    if binary_search(i, wordlist) != None:
        if not i in results:
            results.append(i)

for i in results:
    print(i)
