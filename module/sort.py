#!/usr/bin/python3
"""
A custom module containing some list related algorithms.
Recursion is widely used.
"""
def binary_search(array, item):
    start = 0
    end = len(array) - 1
    while start < end:
        pivot = (end + start) // 2
        if array[pivot] == item:
            return pivot
        elif array[pivot] > item:
            end = pivot
        elif array[pivot] < item:
            start = pivot + 1
    return -1

# Codes for quick sort
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

# Codes for bubble sort.
def switch(ls, index = 0):
    if index >= len(ls) - 1:
        return ls

    elif ls[index] > ls[index + 1]:
        ls[index], ls[index + 1] = ls[index + 1], ls[index]

    return switch(ls, index + 1)

def bubblesort(array):
    if len(array) < 2:
        return array

    switch(array)

    return bubblesort(array[:-1]) + [array[-1]]

# Codes for insertion sort,
def binary_insert(array, item):
    start = 0
    end = len(array) - 1
    pivot = end // 2
    
    while start < end:
        pivot = (end + start) // 2
        if array[pivot] == item:
            return pivot
        elif array[pivot] > item:
            end = pivot
        elif array[pivot] < item:
            start = pivot + 1
    
    return pivot

def insertionsort(array, index = 1):
    for i in range(0, len(array)):
        key = array.pop(i)
        for j in range(i - 1, -1, -1):
            if key > array[j]:
                array.insert(key, j + 1)
            elif j == 0:
                array.insert(key, 0)
        
    return array

# Codes for merge sort.
def merge(a, b):
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

# Codes for heap sort.
def heapsort(array):
    if len(array) <= 1:
        return array
    
    for i in range(len(array) - 1, 0, -1):
        parent = int((i - 1) / 2.0)
        if array[i] > array[parent]:
            array[i], array[parent] = array[parent], array[i]

    return heapsort(array[1:]) + [array[0]]

# General purposed codes for a list.
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
    # for function tests.
    import random
    l = list(x for x in range(10))
    random.shuffle(l)
    print(l)
    print('=' * 50)
    print(insertionsort(l))
