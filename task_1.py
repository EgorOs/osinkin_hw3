#!/usr/bin/env python3


from queue import Queue
# E = dict('A':['B', 'C'], 'B':['C','E'], 'C':['D'])
# E = {"A": ["B", "C"], "B": ["A", "C", "D", "E"], "C": ["A", "B", "E"],
#     "D": ["B"], "E": ["B", "C"], "F":["G"], "G":["F"]}


class Graph:
    def __init__(self, E):
        self.E = E


class GraphIterator:
    def __init__(self, graph, start_v):
        self.graph = graph
        self.current_v = start_v
        self.vertices_left = len(graph)
        self.visited = set()
        self.q = Queue()
        self.q.put(self.current_v)

    def hasNext(self) -> bool:
        self.vertices_left -= 1
        return True if (self.vertices_left + 1) else False

    def next(self) -> str:

        if not self.q.queue:
            self.current_v = [v for v in self.graph.keys() if v not in self.visited][0]
            self.q.put(self.current_v)

        self.current_v = self.q.get()
        self.visited.add(self.current_v)
        for v in self.graph[self.current_v]:
            if v not in self.visited:
                self.q.put(v)
                self.visited.add(v)
        val = self.current_v
        return val


# graph = Graph(E)
# graph_iter = GraphIterator(E, 'F')
# while graph_iter.hasNext():
#     print(graph_iter.next())