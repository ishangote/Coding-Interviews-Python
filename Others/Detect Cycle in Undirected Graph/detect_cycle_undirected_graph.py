"""
BFS Solution: https://www.youtube.com/watch?v=vXrv3kruvwE
"""
from collections import defaultdict
from collections import deque
class GraphVertex:
    def __init__(self, val):
        self.val = val
        self.flag = -1

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def get_adjacent(self, vertex):
        return self.graph[vertex]

def is_cyclic(graph, start_vertex):
    queue = deque([start_vertex])
    start_vertex.flag = 0
    visited = set()

    return bfs(graph, queue, visited)

def bfs(graph, queue, visited):
    while queue:
        vertex = queue.pop()
        for v in graph.get_adjacent(vertex):
            if v.flag == 0: return True
            if v.flag == -1: 
                queue.appendleft(v)
                v.flag = 0

        visited.add(vertex)
        vertex.flag = 1

    return False

import unittest
class TestCycleInUndirectedGraph(unittest.TestCase):
    #Non Cyclic
    a = GraphVertex('a')
    b = GraphVertex('b')
    c = GraphVertex('c')
    d = GraphVertex('d')

    graph = Graph()
    graph.graph[a].append(b)
    graph.graph[a].append(d)
    graph.graph[b].append(a)
    graph.graph[b].append(c)
    graph.graph[c].append(b)
    graph.graph[d].append(a)

    #Cyclic
    _a = GraphVertex('a')
    _b = GraphVertex('b')
    _c = GraphVertex('c')
    _d = GraphVertex('d')

    _graph = Graph()
    _graph.graph[_a].append(_b)
    _graph.graph[_a].append(_c)
    _graph.graph[_a].append(_d)
    _graph.graph[_b].append(_a)
    _graph.graph[_b].append(_c)
    _graph.graph[_c].append(_a)
    _graph.graph[_c].append(_b)
    _graph.graph[_d].append(_a)

    # Test GraphVertex
    def test_graph_vertex_val_flag(self):
        self.assertEqual(self.a.val, 'a')
        self.assertEqual(self.a.flag, -1)

    # Test Graph
    def test_graph_get_adjacent(self):
        self.assertEqual([x.val for x in self.graph.get_adjacent(self.b)], ['a', 'c'])

    # Test is_cyclic
    def test_is_cyclic(self):
        self.assertEqual(is_cyclic(self.graph, self.c), False)
        self.assertEqual(is_cyclic(self._graph, self._b), True)
        
if __name__ == "__main__": unittest.main()