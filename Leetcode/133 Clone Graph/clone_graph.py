import unittest
from collections import deque


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


# Time: O(V + E), where V => number of vertices, E => number of edges
# Space: O(V + E)
def clone_graph(node):
    if not node:
        return None

    node_copy = GraphNode(node.value)
    node_copy_map = {node: node_copy}

    queue = deque([node])

    while queue:
        node = queue.pop()
        for neighbor in node.neighbors:
            if neighbor not in node_copy_map:
                neighbor_copy = GraphNode(neighbor.value)
                node_copy_map[neighbor] = neighbor_copy
                node_copy_map[node].neighbors.append(neighbor_copy)

                queue.append(neighbor)
            else:
                node_copy_map[node].neighbors.append(node_copy_map[neighbor])

    return node_copy


class TestCloneGraph(unittest.TestCase):
    def assert_graph_equal(self, node1, node2, visited):
        if not node1 and not node2:
            return
        self.assertIsNot(node1, node2)
        self.assertEqual(node1.value, node2.value)
        self.assertEqual(len(node1.neighbors), len(node2.neighbors))
        visited.add(node1)

        for i in range(len(node1.neighbors)):
            if node1.neighbors[i] not in visited:
                self.assert_graph_equal(node1.neighbors[i], node2.neighbors[i], visited)

    def test_empty_graph(self):
        self.assertIsNone(clone_graph(None))

    def test_single_node(self):
        node = GraphNode(1)
        cloned = clone_graph(node)
        self.assert_graph_equal(node, cloned, set())

    def test_two_connected_nodes(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

        cloned = clone_graph(node1)
        self.assert_graph_equal(node1, cloned, set())

    def test_three_node_cycle(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]

        cloned = clone_graph(node1)
        self.assert_graph_equal(node1, cloned, set())


if __name__ == "__main__":
    unittest.main()
