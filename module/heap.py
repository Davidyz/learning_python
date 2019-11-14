import math, maths
'''
I did not notice the issue that python's array index start from 0 while in pseudocode it start from 1. As a result, child() and parent() must be modified as below so that the heap algorithms can work properly.
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

class Heap(list):
    def __init__(self, data=[]):
        list.__init__(self, data)
    
    def parent(self, index):
        return math.floor((index - 1) / 2)
    
    def children(self, index):
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        return tuple(i for i in (l, r) if i < len(self))

    def height(self):
        return maths.ln(len(self)) // maths.ln(2)

    def switch(self, a, b):
        '''
        Switch the nodes with index a and b.
        '''
        if 0 <= a < len(self) and 0 <= b < len(self):
            self[a], self[b] = self[b], self[a]

class MaxHeap(Heap):
    def __init__(self, data=[]):
        Heap.__init__(self, data)
    
    def is_max(self):
        for i in range(len(self) - 1, -1, -1):
            if self[self.parent(i)] < self[i]:
                return False
        return True

    def set_pos(self, index):
        '''
        bring a node to a correct position.
        '''
        child = self.children(index)

        while len(child) != 0:  # Check whether it needs to go down (compared with children).
            if len(child) == 1:
                if self[index] < self[child[0]]:
                    self.switch(index, child[0])
                    break
            else:
                if self[child[0]] > self[child[1]]:
                    larger = child[0]
                else:
                    larger = child[1]
                if self[index] < self[larger]:
                    self.switch(index, larger)
                    index = larger
                    child = self.children(index)
                else:
                    break

        parent = self.parent(index)
        while self[index] > self[parent]:   # Check whether it needs to go up (compared with the parent).
            self.switch(index, parent)
            index = parent
            parent = self.parent(index)

    def maxify(self, index=None):
        for i in range(len(self) - 1, -1, -1):
            self.set_pos(i)

    def pop_max(self):
        max_item = self[0]
        self[0] = -math.inf
        self.set_pos(0)
        self.pop(self.index(-math.inf))
        return max_item

    def insert(self, item):
        self.append(item)
        self.set_pos(len(self) - 1)

def pprint(heap, index=0, depth=0):
    if index >= len(heap):
        return 0
    print('  ' * depth + str(heap[index]))
    for i in heap.children(index):
        pprint(heap, i, depth + 1)


if __name__ == '__main__':
    heap = [1,2,3,4,5,6,7,8,9]
    print(heap)
    max_heap(heap)
    print(heap)
