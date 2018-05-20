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
