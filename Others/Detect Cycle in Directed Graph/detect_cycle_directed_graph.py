#Topological Sort Solution
from collections import defaultdict
class GraphVertex:
    def __init__(self, val):
        self.val = val
        self.in_degree = 0

class Graph:
    def __init__(self, vertexes):
        self.graph = defaultdict(set)
        self.vertexes = vertexes

    def set_in_degree(self):
        #Set in_degree for all vertexes
        for vertex in self.graph:
            for v in self.graph[vertex]:
                v.in_degree += 1

    def is_cyclic_topological_sort(self):
        stack = [vertex for vertex in self.vertexes if vertex.in_degree == 0]

        while stack:
            vertex = stack.pop()
            for adjacent in self.graph[vertex]:
                adjacent.in_degree -= 1
                if adjacent.in_degree == 0: stack.append(adjacent)

        for vertex in self.vertexes:
            if vertex.in_degree > 0: return True
        
        return False

import unittest
class TestDetectCycleDirectedGraph(unittest.TestCase):
    
    def test_not_cycle(self):
        a = GraphVertex('a')
        b = GraphVertex('b')
        c = GraphVertex('c')
        d = GraphVertex('d')
        e = GraphVertex('e')
        # Not a cycle
        g = Graph([a, b, c, d, e])

        g.graph[a].add(b)
        g.graph[a].add(c)
        g.graph[b].add(d)
        g.graph[b].add(e)
        g.graph[b].add(c)
        g.graph[d].add(e)

        g.set_in_degree()

        self.assertEqual(g.is_cyclic_topological_sort(), False)

    def test_cycle(self):
        # Cycle
        a = GraphVertex('a')
        b = GraphVertex('b')
        c = GraphVertex('c')
        d = GraphVertex('d')
        e = GraphVertex('e')
        
        g = Graph([a, b, c, d, e])
    
        g.graph[a].add(b)
        g.graph[a].add(c)
        g.graph[b].add(d)
        g.graph[b].add(c)
        g.graph[d].add(e)
        g.graph[e].add(b)

        g.set_in_degree()

        self.assertEqual(g.is_cyclic_topological_sort(), True)

if __name__ == "__main__": unittest.main()