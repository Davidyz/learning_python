"""
A custom module containing some sorting algorithms.
Recursion is widely used.
"""
def quicksort(array):
    if len(array) < 2:
        return array

    mid = array[0]
    more = []
    less = []
    for i in array[1:]:
        if i >= mid:
            more.append(i)
        elif i < mid:
            less.append(i)

    return quicksort(less) + [mid] + quicksort(more)

def quicksort_s(array):
    """
    Quicksort without creating lists other than the original one.
    """
    if len(array) < 2:
        return array
    index = len(array) - 1
    pivot = array.pop(index)
    for i in range(len(array)):
        if array[i] > pivot:
            array.append(array.pop(i))
            index -= 1
        elif i < pivot:
            if i < pivot:
                pass
            else:
                array.insert(0, array.pop(i))
                index += 1
    array.insert(index, pivot)
    return quicksort_s(array[0:index]) + [pivot] + quicksort_s(array[index + 1:])

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

def mergesort(array):
    if len(array) <= 1:
        return array
   
    middle = len(array) // 2
    left = mergesort(array[:middle])
    right = mergesort(array[middle:])
    result = []
    total_len = len(left) + len(right)
    
    while len(result) < len(array):
        if len(left) != 0:
            
            if len(right) != 0:
                
                if left[0] > right[0]:
                    result.append(right.pop(0))
                
                else:
                    result.append(left.pop(0))
            
            elif len(right) == 0:
                for i in range(len(left)):
                    result.append(left[i])
        
        elif len(left) == 0:
            for i in range(len(right)):
                result.append(right[i])
        
        total_len -= 1

    return result
