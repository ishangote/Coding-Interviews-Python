import unittest
from collections import defaultdict, deque


def make_graph(equations, values):
    graph = defaultdict(list)

    for equation, value in zip(equations, values):
        numerator, denominator = equation
        graph[numerator].append((denominator, value))
        graph[denominator].append((numerator, 1 / value))

    return graph


def evaluate_query(query, graph):
    numerator, denominator = query
    if numerator not in graph or denominator not in graph:
        return -1

    visited = set()
    queue = deque([(numerator, 1)])

    while queue:
        node, value = queue.pop()
        visited.add(node)

        if node == denominator:
            return value

        for nbr, nbr_value in graph[node]:
            if nbr in visited:
                continue
            queue.appendleft((nbr, value * nbr_value))

    return -1


# Time: O(q * (V + E)), where q => number of queries, V => number of unique variables, E => number of equations
# Space: O(V + E)
def evaluate_division(equations, values, queries):
    graph = make_graph(equations, values)
    return [evaluate_query(query, graph) for query in queries]


class TestEvaluateDivision(unittest.TestCase):
    def test_basic_case(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        self.assertEqual(evaluate_division(equations, values, queries), expected)

    def test_disconnected_graph(self):
        equations = [["a", "b"], ["c", "d"]]
        values = [2.0, 3.0]
        queries = [["a", "b"], ["c", "d"], ["a", "d"], ["b", "c"]]
        expected = [2.0, 3.0, -1.0, -1.0]
        self.assertEqual(evaluate_division(equations, values, queries), expected)


if __name__ == "__main__":
    unittest.main()
