"""
"""
from graph import *
def has_cycle(graph):
    white = set()
    grey = set()
    black = set()

    for vertex in graph.all_vertex_values:
        white.add(vertex)

    while len(white) > 0:
        current = next(iter(white))
        if has_cycle_util(graph, current, white, grey, black) == True: return True
        
    return False

def has_cycle_util(graph, vertex, white, grey, black):
    move_vertex(vertex, white, grey)

    for neighbor in graph.get_adjacent_vertices(vertex):
        if neighbor in black:
            continue
        if neighbor in grey:
            return True
        if has_cycle_util(graph, neighbor, white, grey, black) == True: return True
        
    move_vertex(vertex, grey, black)
    return False

def move_vertex(v, source_set, dest_set):
    source_set.remove(v)
    dest_set.add(v)

import unittest
class TestIsDirectedGraphCyclic(unittest.TestCase):

    def test_directed_graph_cyclic_generic(self):
        graph1 = Graph()
        graph1.add_edge(1, 2)
        graph1.add_edge(1, 3)
        graph1.add_edge(2, 3)
        graph1.add_edge(4, 1)
        graph1.add_edge(4, 5)
        graph1.add_edge(5, 6)
        graph1.add_edge(6, 4)
        self.assertEqual(has_cycle(graph1), True)

        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        graph.add_edge(4, 1)
        graph.add_edge(4, 5)
        graph.add_edge(5, 6)
        # graph.add_edge(6, 4)
        self.assertEqual(has_cycle(graph), False)

if __name__ == '__main__': unittest.main()