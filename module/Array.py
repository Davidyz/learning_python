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
    return None

# Codes for quick sort
def swap(array, a, b):
    if a != b:
        array[a], array[b] = array[b], array[a]

def find_pivot(array, l, h):
    '''
    Find a better pivot by median of 3 method to avoid the worst case of quicksort.
    '''
    if h - l < 3:
        return l
    if (array[l] <= array[l + 1] and array[l + 1] <= array[l + 2]) or (array[l] > array[l + 1] and array[l + 1] > array[l + 2]):
        swap(array, l, l + 1)
    else:
        if array[l + 1] == max(array[l:l+3]):
            if array[l + 2] > array[l]:
                swap(array, l, l + 2)
        elif array[l + 1] == min(array[l:l + 3]):
            if array[l + 2] < array[l]:
                swap(array, l, l + 2)
    return l
 
def partition(array, l, h):
    '''
    Auxiliary function of quicksort that moves smaller items to the front of the array, 
    and larger items to the end.
    Return the index of the pivot.
    l and h (inclusive) are the start and end of the sub-array to be partitioned.
    '''
    if l == h:
        return l
    bound = l   # the last item in low
    find_pivot(array, l, h)
    for i in range(l + 1, h + 1):
        if array[i] <= array[l]:
            bound += 1
            swap(array, i, bound)

    swap(array, bound, l)
    return bound
   
def quicksort(array):
    stack = [0, len(array) - 1]
    while stack:
        h, l = stack.pop(-1), stack.pop(-1)
        if l > h:
            l, h = h, l
        
        pivot = partition(array, l, h)
        if pivot > l:
            stack.append(l)
            stack.append(pivot - 1)
        if pivot < h:
            stack.append(pivot + 1)
            stack.append(h)
    return array

# Codes for bubble sort.
def switch(ls, index = 0):
    if index >= len(ls) - 1:
        return ls

    elif ls[index] > ls[index + 1]:
        ls[index], ls[index + 1] = ls[index + 1], ls[index]

    return switch(ls, index + 1)

def shellsort(array, factor = None):
    step = len(array) - 1
    if step == 0 or len(array) <= 1:
        return array

    if factor == None:
        factor = 1/2

    while True:
        i = 0
        unswaped = True
        while i + step < len(array): 
            
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                unswaped = False
            
            i += 1

        if unswaped and step > 1:
            step = int(factor * step)
        elif step <= 1 and unswaped:
            break

    return array

def bubblesort(array):
    end = len(array)

    while end != 0:
        for i in range(end - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        end -= 1
    return array

# Codes for insertion sort.
def binary_insert(array, end, item):
    '''
    Return the index to insert the item.
    '''
    start = 0

    while start != end:
        middle = (start + end) // 2
        if array[middle] >= item:
            end = middle - 1
        elif array[middle] < item:
            start = middle + 1
    
    if item < array[start]:
        return start
    else:
        return start + 1

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
