class Node():
    def __init__(self, adj=None, t_d=0, t_f=0):
        self._adj = adj
        self._pre = None
        self.t_discover = t_d
        self.t_finish = t_f
        self._status  = ''  # 'undiscovered', 'exploring' or 'done'
    
    def status(self, status=None):
        if status == None:
            return self._status
        elif status == str:
            self._status = status

    def predecessor (self, node=None):
        if node == Node:
            self._pre = node
        elif node == None:
            return self._pre

    def adjacency(self, adj=None):
        if adj == None:
            return self._adj
        else:
            self._adj = adj

    def explore(self, time):
        time += 1
        self.t_discover = time
        self._status = 'exploring'

        for i in adj:
            if i.status() == 'undiscovered':
                i.add_predecessor(self)
                i.explore(time)
        
        time += 1
        self.t_finish = time
        self._status = 'done'

    def dump(self):
        result = (self.t_discover, self.t_finish, self._pre)
        print(result)
        return result

def DFS(graph, start):
    if start != 0:
        graph[start], graph[0] = graph[0], graph[start]

    for i in graph:
        i.status('undiscovered')

    time = 0
    for i in graph:
        if i.status() == 'undiscovered':
            i.explore(time)

if __name__ == '__main__':
    Graph = []
    for i in range(8):
        Graph.append(Node())
    
    Graph[0].adjacency([Graph[1], Graph[2], Graph[3]]) #a
    Graph[1].adjacency([Graph[2], Graph[3]]) #b
    Graph[2].adjacency([Graph[0]]) #c
    Graph[3].adjacency([Graph[2]]) #d
    Graph[4].adjacency([Graph[3], Graph[5]]) #e
    Graph[5].adjacency([Graph[3]]) #f
    Graph[6].adjacency([Graph[4], Graph[5], Graph[7]]) #g
    Graph[7].adjacency([Graph[3]]) #h

    DFS(Graph, 0)
    for i in Graph:
        i.dump()
