"""
A custom module contaaining some sorting algorithms.
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

def bubblesort(array):
    if len(array) < 2:
        return array

    def switch(ls, index = 0):
        if index >= len(ls) - 2:
            return ls

        elif ls[index] > ls[index + 1]:
            ls[index], ls[index + 1] = ls[index + 1], ls[index]
            
        return switch(ls, index + 1)
    
    switch(array)

    return bubblesort(array[:-1]) + [array[-1]]

def insertsort(array, index = 1):
    # NOT FINISHED!!!
    if index == len(array):
        return array

    else:
        for i in range(index - 1, -1, -1):

            if i == 0:
                array.insert(0, array.pop(index))

            elif array[i] <= array[index]:
                array.insert(i + 1, array.pop(index))

    return insertsort(array, index + 1)
