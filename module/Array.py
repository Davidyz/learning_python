#!/usr/bin/python3
"""
A custom module containing some list related algorithms and queues.
Recursion is widely used.
"""
from math import ceil
import heap

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
def pivot(array):
    pass

def median3(array):
    if len(array) == 3:
        return 3 - array.index(max(array)) - array.index(min(array))

def quicksort(array):
    if len(array) < 2:
        return array
    
    if len(array) >= 3:
        array[median3(array[:3])], array[-1] = array[-1], array[median3(array[:3])]

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
def insertionsort(array, index = 1):
    if len(array) == 1:
        return array
    boundary = 1
    while boundary < len(array):
        if array[boundary] >= array[boundary - 1]:
            pass
        elif array[boundary] <= array[0]:
            array.insert(0, array.pop(boundary))

        else:
            for i in range(boundary):
                if array[i] <= array[boundary] <= array[i + 1]:
                    array.insert(i + 1, array.pop(boundary))
        boundary += 1
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
    middle = len(array) // 2
    return merge(mergesort(array[:middle]), mergesort(array[middle:]))

def mergesort_loop(array):
    max_len = len(array)
    queue = [array]
    
    while len(queue) < max_len:
        temp = queue.pop(0)
        if len(temp) == 1:
            queue.append(temp)
            continue

        divider = len(temp) // 2
        queue.append(temp[:divider])
        queue.append(temp[divider:])

    while len(queue) > 1:
        l1 = queue.pop(0)
        l2 = queue.pop(0)
        queue.append(merge(l1, l2))

    return queue[0]

# Codes for heap sort. Not in working order yet.

def heapsort(array):
    array = heap.MaxHeap(array)
    array.maxify()
    new_array = []
    while array:
        new_array.insert(0, array.pop_max())
    return new_array

# General purposed codes for a list.
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def reversed(array):
    return list(array[i] for i in range(len(array) - 1, -1, -1))

def clear_item(array, item):
    '''
    Clear however many of an item from the array.
    '''
    for i in range(array.count(item)):
        array.remove(item)
    return array

if __name__ == '__main__':
    # for function tests.
    import random
    array = list(i for i in range(100))
    random.shuffle(array)
    print(array)
    print('=' * 100)
    array = heapsort(array)
    print(array)
    print(is_sorted(array))
