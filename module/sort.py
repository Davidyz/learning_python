#!/usr/bin/python3
"""
A custom module containing some sorting algorithms.
Recursion is widely used.
"""
def quicksort(array):
    if len(array) < 2:
        return array
    
    pivot = array[-1]
    i = 0
    j = len(array) - 1
    
    while i < j:
        if array[i] <= pivot:
            i += 1
        elif array[i] > pivot:
            array.insert(-1, array.pop(i))
            j -= 1
    return quicksort(array[:j]) + [pivot] + quicksort(array[j:len(array) - 1])

def bubblesort(array):
    if len(array) < 2:
        return array

    def switch(ls, index = 0):
        if index >= len(ls) - 1:
            return ls

        elif ls[index] > ls[index + 1]:
            ls[index], ls[index + 1] = ls[index + 1], ls[index]

        return switch(ls, index + 1)
    
    switch(array)

    return bubblesort(array[:-1]) + [array[-1]]

def insertionsort(array, index = 1):
    for i in range(1, len(array)):
        key = array.pop(i)
        j = i
        while j > 0 and array[j - 1] > key:
            j -= 1
        array.insert(j, key)
    return array

def merge(a, b):
    '''
    if not a:
        return b
    if not b:
        return a
    '''
    output = []
    while len(a) * len(b) != 0:
        if a[0] < b[0]:
            output.append(a.pop(0))
        
        else:
            output.append(b.pop(0))
    
    for i in a:
        output.append(i)
    for i in b:
        output.append(i)
    return output

def mergesort(array):
    if len(array) < 2:
        return array
    middle = int(len(array) / 2)
    return merge(mergesort(array[:middle]), mergesort(array[middle:]))

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def reversed(array):
    result = []
    for i in array:
        result.insert(0, i)
    return result

if __name__ == '__main__':
    import random
    l = list(x for x in range(100))
    random.shuffle(l)
    print(l)
    print('=' * 50)
    print(insertionsort(l))
    print(l)
