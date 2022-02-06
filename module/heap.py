import math, maths

"""
I did not notice the issue that python's array index start from 0 while in pseudocode it start from 1. As a result, child() and parent() must be modified as below so that the heap algorithms can work properly.
"""


def is_max(heap, index=None):
    if index == None:
        index = len(heap) - 1

    while index > 0:
        if heap[index] > heap[parent(index)]:
            return False
        index -= 1

    return True


class Heap(list):
    def __init__(self, data=[]):
        list.__init__(self, data)

    def __str__(self):
        return str(list(self))

    def __repr__(self, index=0, depth=0):
        string = ""
        if index >= len(self):
            return string

        for i in range(depth):
            string += "|   "
        string += str(self[index]) + "\n"
        for i in self.children(index):
            string += self.__repr__(i, depth + 1)

        return string

    def height(self):
        for i in range(len(self) - 1, -1, -1):
            if self[i] != None:
                return math.floor(math.log2(i + 1))
        return 0

    def parent(self, index):
        return math.floor((index - 1) / 2)

    def children(self, index):
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        return tuple(i for i in (l, r) if i < len(self))

    def switch(self, a, b):
        """
        Switch the nodes with index a and b.
        """
        if 0 <= a < len(self) and 0 <= b < len(self):
            self[a], self[b] = self[b], self[a]

    def add_child(self, index, value):
        if not index < len(self):
            raise IndexError("Adding child to a non-existing node.")

        target_index = 2 * index + 1
        if target_index < len(self):
            if self[target_index] != None:
                if not target_index + 1 < len(self):
                    self.append(None)
                if self[target_index + 1] == None:
                    target_index += 1

            elif self[target_index] != None and self[target_index + 1] != None:
                raise ValueError("The node has no empty room for children.")

        while len(self) <= ((target_index + 1) // 2) * 2:
            self.append(None)
        self[target_index] = value
        return self


class MaxHeap(Heap):
    def __init__(self, data=[]):
        Heap.__init__(self)
        for i in data:
            self.add(i)

    def height(self):
        return math.floor(math.log2(len(self)))

    def max_child(self, node):
        if len(self.children(node)) == 2:
            if self[self.children(node)[0]] > self[self.children(node)[1]]:
                return self.children(node)[0]
            else:
                return self.children(node)[1]

        elif len(self.children(node)) == 1:
            return self.children(node)[0]
        else:
            return None

    def make_max(self, index):
        if index != 0 and self[index] > self[self.parent(index)]:
            self.switch(index, self.parent(index))
            self.make_max(self.parent(index))

        max_leaf = self.max_child(index)

        if max_leaf != None and self[index] < self[self.max_child(index)]:
            self[index], self[max_leaf] = self[max_leaf], self[index]
            self.make_max(max_leaf)

        return self

    def pop_max(self):
        if len(self) > 1:
            max_item = self[0]
            self[0] = self.pop(-1)
            self.make_max(0)
            return max_item
        else:
            return self.pop(0)

    def add(self, item):
        self.append(item)
        self.make_max(len(self) - 1)

    def add_child(self, item, value):
        # arbitary addition not allowed. using max_heap addition to maintain max_heap structure.
        self.add(value)


def heap_sort(array):
    heap = MaxHeap(array)
    array = []
    while heap:
        array.insert(0, heap.pop_max())
    return array


def pprint(heap, index=0, depth=0):
    if index >= len(heap):
        return 0
    print("  " * depth + str(heap[index]))
    for i in heap.children(index):
        pprint(heap, i, depth + 1)


if __name__ == "__main__":
    h = MaxHeap(range(50))
    print(h)
