#!/usr/bin/env python3
import itertools, sys
sys.path.append('/home/david/git/learning_python/module/')
import sort

fin = open('wordplay/new_google-10000-english.txt', 'r')
wordlist = fin.readlines()
fin.close()
wordlist = list(i[:-1].lower() for i in wordlist)

if len(sys.argv) == 2:
    letters = str(sys.argv[-1]).lower()
else:
    print('Invalid argument!')
    exit()

results = []

def binary_search(word, array, start=0, end=None):
    
    if end == None:
        end = len(array) - 1
    if start == end:
        if word == array[start]:
            return start
        else:
            return None
    
    elif start < end:
        middle = (start + end) // 2
        
        if word == array[middle]:
            return middle
        
        elif word > array[middle]:
            return binary_search(word, array, middle + 1, end)
        
        elif word < array[middle]:
            return binary_search(word, array, start, middle - 1)

for i in range(len(letters)):
    for j in itertools.permutations(letters, i):
        j = ''.join(j)
        if binary_search(j, wordlist) != None:
            if not j in results: #j binary_search(j, results) == -1:
                print(j)
                results.append(j)
