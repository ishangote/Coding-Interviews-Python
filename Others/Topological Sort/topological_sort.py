import unittest
from collections import defaultdict


class CycleDetectedError(Exception):
    """Custom exception for detecting cycles in a graph."""

    pass


def topological_sort_kahn(graph, num_vertices):
    res = []
    in_degree = [0] * num_vertices

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    stack = [vertex for vertex in range(num_vertices) if in_degree[vertex] == 0]

    while stack:
        vertex = stack.pop()
        res.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    for degree in in_degree:
        if degree > 0:
            raise CycleDetectedError(
                "Graph has a cycle, topological sort is not possible"
            )

    return res


class TestTopologicalSort(unittest.TestCase):
    def test_acyclic_graph(self):
        # Graph:
        # 5 -> 0 -> 4
        # 5 -> 2 -> 3
        # 4 -> 1
        graph = defaultdict(list)
        graph[5].extend([0, 2])
        graph[0].append(4)
        graph[2].append(3)
        graph[4].append(1)

        self.assertIn(
            topological_sort_kahn(graph, 6), [[5, 0, 2, 4, 3, 1], [5, 2, 3, 0, 4, 1]]
        )

    def test_disconnected_graph(self):
        # Graph: 0 -> 1, 2 -> 3 (disconnected components)
        graph = defaultdict(list)
        graph[0].append(1)
        graph[2].append(3)

        # Expected topological order (valid orders depend on graph structure)
        self.assertIn(
            topological_sort_kahn(graph, 4), [[0, 2, 1, 3], [2, 0, 3, 1], [2, 3, 0, 1]]
        )

    def test_cyclic_graph(self):
        # Graph: 0 -> 1 -> 2 -> 0 (cycle)
        graph = defaultdict(list)
        graph[0].append(1)
        graph[1].append(2)
        graph[2].append(0)

        # Expect CycleDetectedError
        with self.assertRaises(CycleDetectedError):
            topological_sort_kahn(graph, 3)


if __name__ == "__main__":
    unittest.main()
