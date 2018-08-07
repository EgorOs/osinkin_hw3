#!/usr/bin/env python3


from queue import Queue
# E = dict('A':['B', 'C'], 'B':['C','E'], 'C':['D'])
E = {"A": ["B", "C"], "B": ["A", "C", "D", "E"], "C": ["A", "B", "E"], "D": ["B", "F"], "E": ["B", "C"], "F":["D"]}


class Graph:
    def __init__(self, E):
        self.E = E


class GraphIterator:
    def __init__(self, graph, start_v):
        self.graph = graph
        self.current_v = start_v

        self.visited = set()
        self.q = Queue()
        self.q.put(self.current_v)

    def hasNext(self) -> bool:
        return True if len(self.q.queue) != 0 else False

    def next(self) -> str:
        #  print(self.q.queue)
        self.current_v = self.q.get()
        self.visited.add(self.current_v)
        for v in self.graph[self.current_v]:
            if v not in self.visited:
                self.q.put(v)
                self.visited.add(v)
        val = self.current_v
        return val

graph = Graph(E)
graph_iter = GraphIterator(E, 'F')
while graph_iter.hasNext():
    print(graph_iter.next())