import unittest
from collections import defaultdict, deque


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def generate_graph(node, parent, graph):
    if not node:
        return

    if parent:
        graph[node.value].append(parent.value)

    if node.left:
        graph[node.value].append(node.left.value)
        generate_graph(node.left, node, graph)

    if node.right:
        graph[node.value].append(node.right.value)
        generate_graph(node.right, node, graph)


# Time: O(n), where n => number of nodes in BT
# Space: O(n)
def distance_k(root, target, k):
    graph = defaultdict(list)
    generate_graph(root, None, graph)

    visited, queue = set(), deque([(target, k)])
    res = []

    while queue:
        node_value, distance = queue.pop()

        visited.add(node_value)

        if distance == 0:
            res.append(node_value)

        else:
            for neighbor in graph[node_value]:
                if neighbor not in visited:
                    queue.appendleft((neighbor, distance - 1))

    return res


class TestDistanceKNodes(unittest.TestCase):
    def test_distance_k_nodes_edge(self):
        self.assertEqual(distance_k(BTNode(3), 3, 100), [])

    def test1_distance_k_nodes(self):
        root = BTNode(3)

        root.left = BTNode(5)
        root.right = BTNode(1)

        root.left.left = BTNode(6)
        root.left.right = BTNode(2)
        root.right.left = BTNode(0)
        root.right.right = BTNode(8)

        root.left.right.left = BTNode(7)
        root.left.right.right = BTNode(4)

        self.assertListEqual(distance_k(root, 5, 2), [1, 7, 4])
        self.assertListEqual(distance_k(root, 3, 2), [6, 2, 0, 8])
        self.assertListEqual(distance_k(root, 3, 3), [7, 4])


if __name__ == "__main__":
    unittest.main()
