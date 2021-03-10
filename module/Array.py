#!/usr/bin/python3
"""
A custom module containing some list related algorithms and queues.
Recursion is widely used.
"""
from math import ceil
import heap
import time

def insert(array, source, target):
    if source > target:
        item = array[source]
        for i in range(source, target - 1, -1):
            array[i] = array[i - 1]
        array[target] = item
    elif source < target:
        item = array[source]
        for i in range(source, target + 1):
            array[i] = array[i + 1]
        array[target] = item
    else:
        pass
    return array

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
   
def quicksort(array, heuristics=False):
    '''
    Implemented with stack and while loop, so that this is an in-place and non-recursive function.
    heuristics: use is_sorted to check whether the subarray is already sorted.
    Should improve the performance on already-sorted arrays.
    '''
    stack = [0, len(array) - 1]
    while stack:
        h, l = stack.pop(-1), stack.pop(-1)
        if l > h:
            l, h = h, l
        
        pivot = partition(array, l, h)
        if heuristics and is_sorted(array[l:h + 1]):
            continue
        if pivot > l:
            stack.append(l)
            stack.append(pivot - 1)
        if pivot < h:
            stack.append(pivot + 1)
            stack.append(h)
    return array

# Codes for bubble sort.
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
def binary_insert(array, tail, item):
    '''
    Return the index to insert the item.
    '''
    start = 0
    end = tail

    while start < end:
        middle = (start + end) // 2
        if array[middle] >= item:
            end = middle - 1
        elif array[middle] < item:
            start = middle + 1
    
    if item < array[start]:
        return start
    else:
        return min(start + 1, tail)

def insertionsort(array, index = 1, binary=True):
    if len(array) == 1:
        return array
    boundary = 1
    while boundary < len(array):
        if array[boundary] >= array[boundary - 1]:
            pass
        elif binary:
            index = binary_insert(array, boundary - 1, array[boundary])                                        
            array.insert(index, array.pop(boundary))

        else:
            if array[boundary] <= array[0]:
                array.insert(0, array.pop(boundary))
            else:
                for i in range(boundary):
                    if array[i] <= array[boundary] <= array[i + 1]:
                        array.insert(i + 1, array.pop(boundary))
        boundary += 1
    return array

# Codes for merge sort.
def merge(a, b):
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]
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

def merge_loop(array, l, m, h):
    '''
    The in_place vertion of merge()
    l is the index of the first item of the first array.
    m is the the index of the first item of the second array.
    h is 1 + the index after the last item of the second array.
    '''
    if not (l < m < h):
        return array

    while l < m and m < h:
        if array[l] > array[m]:
            insert(array, m, l)
            l += 1
            m += 1
        elif array[l] == array[m]:
            insert(array, m, l + 1)
            l += 2
            m += 1
        else:
            l += 1

    return array

def mergesort_loop(array):
    max_len = len(array)
    queue = []
    t = 0
    start = time.time()

    for i in range(len(array)):
        queue += [i, i + 1]

    while len(queue) > 2:
        l = queue.pop(0)
        m = queue.pop(0)
        if m == queue[0]:
            queue.pop(0)
            h = queue.pop(0)
            t -= time.time()
            merge_loop(array, l, m, h)
            t += time.time()
            queue += [l, h]
        else:
            queue += [l, m]

    return array, t, time.time() - start

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
    import random, sys
    
    if sys.argv == []:
        n = 100
    else:
        n = int(sys.argv[1])
    array = list(i for i in range(n))
    random.shuffle(array)
    print(array)
    print('=' * 100)
    array = mergesort_loop(array)
    print(array)
    print(is_sorted(array))
