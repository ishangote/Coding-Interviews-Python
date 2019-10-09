import heapq
#Priority queue implementation
def dijkstras(graph, start_node):
    distances = {nodes: float('inf') for nodes in graph}
    distances[start_node] = 0
    q = [(0, start_node)]

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if curr_dist > distances[curr_node]: continue

        for neighbor, wt in graph[curr_node].items():
            distance = curr_dist + wt
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))

    return distances

#UNIT TESTING...

import unittest
class TestDijkstrasAlgorithm(unittest.TestCase):
    def test_edge_cases(self):
        #graph with no edges
        graph = {
        'a': {},
        'b': {},
        'c': {}
        }
        self.assertEqual(dijkstras(graph, 'a'), {'a': 0, 'b': float('inf'), 'c': float('inf')})

    def test_generic_case(self):
        graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1}
        }
        self.assertEqual(dijkstras(graph, 'X'), {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2})

    # ASSIGNMENT 3 EXAMPLE...
    def test_given_example(self):
        
        network = {
        'h1': {'h1': 0, 'h2': 10, 'h3': 5, 'h6': 15, 'h7': 15, 's3': 10},
        'h2': {'h2': 0, 'h1': 10, 'h6': 15, 'h7': 15},
        'h3': {'h3': 0, 'h1': 5, 'h5': 5},
        'h5': {'h5': 0, 'h3': 5, 'h6': 10, 'h7': 10},
        'h6': {'h6': 0, 'h2': 15, 'h5': 10, 'h1': 15, 'h7': 0, 's3': 5},
        'h7': {'h7': 0, 'h2': 15, 'h5': 10, 'h1': 15, 'h6': 0, 's3': 5},
        's3': {'s3': 0, 'h1': 10, 'h6': 5, 'h7': 5}
        }

        #FROM h1 to all
        self.assertEqual(dijkstras(network, 'h1'), {'h1': 0, 'h2': 10, 'h3': 5, 'h5': 10, 'h6': 15, 'h7': 15, 's3': 10})

        #FROM h2 to all
        self.assertEqual(dijkstras(network, 'h2'), {'h1': 10, 'h2': 0, 'h3': 15, 'h5': 20, 'h6': 15, 'h7': 15, 's3': 20})

        #FROM h3 to all
        self.assertEqual(dijkstras(network, 'h3'), {'h1': 5, 'h2': 15, 'h3': 0, 'h5': 5, 'h6': 15, 'h7': 15, 's3': 15})

        #FROM h5 to all
        self.assertEqual(dijkstras(network, 'h5'), {'h1': 10, 'h2': 20, 'h3': 5, 'h5': 0, 'h6': 10, 'h7': 10, 's3': 15})

        #FROM h6 to all
        self.assertEqual(dijkstras(network, 'h6'), {'h1': 15, 'h2': 15, 'h3': 15, 'h5': 10, 'h6': 0, 'h7': 0, 's3': 5})

        #FROM h7 to all
        self.assertEqual(dijkstras(network, 'h7'), {'h1': 15, 'h2': 15, 'h3': 15, 'h5': 10, 'h6': 0, 'h7': 0, 's3': 5})

if __name__ == "__main__": unittest.main()