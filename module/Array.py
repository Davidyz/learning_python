#!/usr/bin/python3
"""
A custom module containing some list related algorithms and queues.
Recursion is widely used.
"""
from math import ceil
import heap
import time, collections, random

class SortingError(Exception):
    pass

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

def binary_search(array, item, start=0, end=None):
    start = 0
    if end == None:
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
    stack = collections.deque()
    stack.append(0)
    stack.append(len(array) - 1)

    while stack:
        h, l = stack.pop(), stack.pop()
        
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
def shellsort(array, factor = 1/2):
    step = len(array) - 1
    if step == 0 or len(array) <= 1:
        return array

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
def binary_insert(array, start, tail, item):
    '''
    Return the index to insert the item.
    start and end are both inclusive.
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
            index = binary_insert(array, 0, boundary - 1, array[boundary])                                        
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
        # iterate through the second sub-array from the head and insert items into the first array.
        if array[m] < array[m - 1]:
            array.insert(binary_insert(array, l, m - 1, array[m]), array.pop(m))
        m += 1

    return array

def mergesort_loop(array, heuristics=True):
    max_len = len(array)
    queue = collections.deque()
    
    i = 0
    while i < len(array):
        # generate a queue of indices of the starts and ends of sorted sub_arrays.
        start = i
        queue.append(i)
        if heuristics and i < len(array) - 1:
            if array[i] <= array[i + 1]:
                while i < len(array) - 1 and array[i] <= array[i + 1]:
                    i += 1
            elif i < len(array) - 1 and array[i] < array[i + 1]:
                while array[i] <= array[i + 1]:
                    i += 1
                reversed_list(array, start, i, in_place=True)

        queue.append(i + 1)
        i += 1

    while len(queue) > 2:
        # merge the sub_arrays
        l = queue.popleft()
        m = queue.popleft()
        if m == queue[0]:
            queue.popleft()
            h = queue.popleft()
            merge_loop(array, l, m, h)
            queue.append(l)
            queue.append(h)
        else:
            queue.append(l)
            queue.append(m)

    return array

# Codes for heap sort.
def parent(n):
    '''
    return the index of the parent node.
    '''
    if n == 0:
        return 0
    return (n - 1) // 2

def child(n):
    '''
    return the indices of the child nodes.
    '''
    first = 2 * n + 1
    return first, first + 1

def maxify(array, end):
    '''
    end: the index of the last item in the array, also the item to be added in the heap.
    '''
    index = end
    while index != 0:
        if index == 0:
            break
        if array[index] > array[parent(index)]:
            array[index], array[parent(index)] = array[parent(index)], array[index]
            index = parent(index)
        else:
            break
    return array

def heapsort(array):
    for i in range(len(array)):
        array = maxify(array, i)

    for end in range(len(array) - 1, -1, -1):
        array[end], array[0] = array[0], array[end]
        index = 0
        while True:
            indices = [i for i in child(index) if i < end]
            if len(indices) != 0:
                child_node = indices[0]
                if len(indices) == 2 and array[indices[1]] > array[child_node]:
                    child_node = indices[1]
                if array[child_node] > array[index]:
                    array[child_node], array[index] = array[index], array[child_node]
                    index = child_node
                else:
                    break
            else:
                break
    return array

# General purposed codes for a list.
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def reversed_list(array, start=0, end=None, in_place=False):
    if end == None:
        end = len(array)
    if not in_place:
        return list(array[i] for i in range(end - 1, start - 1, -1))
    else:
        for i in range(start, start + (end - start) // 2):
            swap(array, i, end - (i - start) - 1)
        return array

def clear_item(array, item):
    '''
    Clear however many of an item from the array.
    '''
    for i in range(array.count(item)):
        array.remove(item)
    return array

def randtest(func, length=1000, repeat=5, typ = int, extra_args=[], ordered=False):
    '''
    Pass any extra arguments by setting the parameter extra_args as a list.
    the ordered parameter allows testing with sorted array, which, in some cases, can be used as a worst-case test.
    '''
    l = [typ(i) for i in range(length)]
    
    time_accu = 0
    for i in range(repeat):
        temp_list = l.copy()

        if not ordered:
            random.shuffle(temp_list)

        time_accu -= time.time()
        sorted_array = func(temp_list, *extra_args)
        time_accu += time.time()

        if not is_sorted(sorted_array):
            raise SortingError("The list is not sorted.")

    return time_accu / repeat

def entropy(array):
    '''
    Return a number that measure how sorted the array is. 0 for sorted.
    '''
    count_p = 0
    count_n = 0

    for i in range(len(array) - 1):
        count_p += int(array[i] <= array[i + 1])
        count_n += int(array[i] >= array[i + 1])

    return 1 - max(count_p, count_n) / (len(array) - 1)

if __name__ == '__main__':
    # for function tests.
    import random, sys

    length = 1000000
    mergesort_time = randtest(mergesort_loop, length, repeat=10, extra_args=[True])
    insertionsort_time = randtest(insertionsort, length, repeat=10, extra_args=[False])
    print("MergeSort:\t", mergesort_time)
    print("InsertionSort:\t", insertionsort_time)
