import math
'''
I did not notice the issue that python's array index start from 0 while in pseudocode it start from 1. As a result, the way in which child() and parent() work must be modified as below so that the heap algorithms can work properly.
'''
def parent(index):
    return math.floor((index - 1) / 2)

def child(index):
    l = (index + 1) * 2 - 1
    r = (index + 1) * 2 
    return l, r

def is_max(heap, index=None):
    if index == None:
        index = len(heap) - 1

    while index > 0:
        if heap[index] > heap[parent(index)]:
            return False
        index -= 1

    return True

def maxify(heap, index=0):
    '''
    Move the item specified by index to the place it should be at.
    '''
    l_child , r_child = child(index)

    if (l_child < len(heap)) and (heap[index] < heap[l_child]):
        largest = l_child
    else:
        largest = index

    if (r_child < len(heap)) and (heap[largest] < heap[r_child]):
        largest = r_child

    if index != largest:
        heap[index], heap[largest] = heap[largest], heap[index]
        maxify(heap, largest)

def max_heap(heap):
    for i in range(parent(len(heap) - 1), -1, -1):
        maxify(heap, i)
    return heap

def remove_max(heap):
    item = heap[0]
    heap[0] = heap.pop()
    heap = maxify(heap, 0)
    return item

if __name__ == '__main__':
    heap = [1,2,3,4,5,6,7,8,9]
    print(heap)
    max_heap(heap)
    print(heap)
