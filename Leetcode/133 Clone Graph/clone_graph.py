import unittest
from collections import deque


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    # Make GraphNode hashable so it can be used as a dictionary key.
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other


# ------------------ DFS Solution ------------------ #


def recursive_helper(old_node, visited_old_new_map):
    if not old_node:
        return None

    if old_node not in visited_old_new_map:
        new_node = GraphNode(old_node.value)
        visited_old_new_map[old_node] = new_node
        new_node.neighbors = [
            recursive_helper(old_nbr, visited_old_new_map)
            for old_nbr in old_node.neighbors
        ]

    return visited_old_new_map[old_node]


# Time: O(n), where n => number of nodes in graph
# Space: O(n)
def clone_graph_dfs(node):
    return recursive_helper(node, {})


# ------------------ BFS Solution ------------------ #


# Time: O(V + E), where V => number of vertices, E => number of edges
# Space: O(V + E)
def clone_graph_bfs(node):
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


# ------------------ Unit Tests ------------------ #
class TestCloneGraph(unittest.TestCase):
    def assert_graph_equal(self, node1, node2, visited=None):
        if visited is None:
            visited = set()

        # Both nodes should be None, or both not None.
        if node1 is None and node2 is None:
            return
        self.assertIsNot(node1, node2)  # Cloned nodes must be new instances.
        self.assertEqual(node1.value, node2.value)
        self.assertEqual(len(node1.neighbors), len(node2.neighbors))
        visited.add(node1)

        # Check each corresponding neighbor.
        for n1, n2 in zip(node1.neighbors, node2.neighbors):
            if n1 not in visited:
                self.assert_graph_equal(n1, n2, visited)

    def run_clone_tests(self, clone_function):
        # Test 1: Empty graph.
        self.assertIsNone(clone_function(None))

        # Test 2: Single node graph.
        node = GraphNode(1)
        clone = clone_function(node)
        self.assert_graph_equal(node, clone)

        # Test 3: Two connected nodes.
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        clone = clone_function(node1)
        self.assert_graph_equal(node1, clone)

        # Test 4: Three-node cycle.
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]
        clone = clone_function(node1)
        self.assert_graph_equal(node1, clone)

    def test_clone_graph_dfs(self):
        self.run_clone_tests(clone_graph_dfs)

    def test_clone_graph_bfs(self):
        self.run_clone_tests(clone_graph_bfs)


if __name__ == "__main__":
    unittest.main()
