from math import inf
import Array

class Node():
    def __init__(self, adj=None, t_d=0, t_f=0, value = None):
        self._adj = adj
        self.predecessor = None
        self.t_discover = t_d
        self.t_finish = t_f
        self.distance = inf
        self.status  = ''  # 'undiscovered', 'exploring' or 'done'
        self.key = value
    
    '''
    def status(self, status=None):
        if status == None:
            return self._status
        elif status == str:
            self.status = status

    def predecessor (self, node=None):
        if node == Node:
            self.pre = node
        elif node == None:
            return self.pre
    '''
    def adjacency(self, adj=None):
        if adj == None:
            return self._adj
        else:
            self._adj = adj

    def explore(self, time):
        time += 1
        self.t_discover = time
        self.status = 'exploring'

        for i in self._adj:
            if i.status == 'undiscovered':
                i.predecessor = self
                time = i.explore(time)
        
        time += 1
        self.t_finish = time
        self.status = 'done'
        return time

    def dump(self, info):
        if info == 'distance':
            if self.predecessor != None:
                result = (self.distance, self.predecessor.key)
            else:
                result = (self.distance, None)

        if info == 'time':
            if self.predecessor != None:
                result = (self.t_discover, self.t_finish, self.predecessor.key)
            else:
                result = (self.t_discover, self.t_finish, None)

        print(result)
        return result

def DFS(graph, start):
    if start != 0:
        graph[start], graph[0] = graph[0], graph[start]

    for i in graph:
        i.status = 'undiscovered'
        i.adjacency(None)

    time = 0
    for i in graph:
        if i.status == 'undiscovered':
            time = i.explore(time)

def BFS(graph, start):
    if start != 0:
        graph[start], graph[0] = graph[0], graph[start]

    graph[0].distance = 0
    queue = []
    queue.append(graph[0])

    while queue:
        u = queue.pop(0)
        for i in u.adjacency():
            if i.distance == inf:
                i.distance = u.distance + 1
                i.predecessor = u
                queue.append(i)

if __name__ == '__main__':
    Graph = []
    for i in range(8):
        Graph.append(Node(value = i))
    
    Graph[0].adjacency([Graph[1], Graph[3], Graph[4]]) #a
    Graph[1].adjacency([Graph[2], Graph[3]]) #b
    Graph[2].adjacency([Graph[0]]) #c
    Graph[3].adjacency([Graph[2]]) #d
    Graph[4].adjacency([Graph[3], Graph[5]]) #e
    Graph[5].adjacency([Graph[3]]) #f
    Graph[6].adjacency([Graph[4], Graph[5], Graph[7]]) #g
    Graph[7].adjacency([Graph[3]]) #h

    DFS(Graph, 0)
    for i in Graph:
        print(i.key, end=' ')
        i.dump('time')
