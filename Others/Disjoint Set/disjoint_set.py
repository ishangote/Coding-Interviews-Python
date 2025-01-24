import unittest


class DSNode:
    """
    Represents a node in the disjoint set.
    Each node has a value, a rank (used for balancing), and a parent pointer.
    """

    def __init__(self, value):
        self.value = value
        self.rank = 0  # Rank is used to keep the tree shallow during union operations
        self.parent = self  # Each node is initially its own parent


class DisjointSet:
    """
    Implementation of the Disjoint Set (Union-Find) data structure
    with path compression and union by rank.
    """

    def __init__(self):
        self.node_map = {}  # Maps values to their corresponding DSNode instances

    def make_set(self, value):
        """
        Creates a new set containing the given value.
        Each value starts as its own set with itself as the parent.
        """
        if value not in self.node_map:
            self.node_map[value] = DSNode(value)

    def union(self, value1, value2):
        """
        Merges the sets containing value1 and value2.
        Uses union by rank to keep the tree balanced.
        """
        node1, node2 = self.node_map[value1], self.node_map[value2]

        # Find the roots (representatives) of the sets for both values
        root1 = self.find_set_node(node1)
        root2 = self.find_set_node(node2)

        # If they are already in the same set, do nothing
        if root1 == root2:
            return

        # Union by rank: attach the smaller tree under the larger tree
        if root1.rank > root2.rank:
            root2.parent = root1
        elif root1.rank < root2.rank:
            root1.parent = root2
        else:
            # If ranks are the same, arbitrarily attach root2 under root1 and increase root1's rank
            root2.parent = root1
            root1.rank += 1

    def find_set(self, value):
        """
        Finds and returns the representative (root) value of the set containing the given value.
        Uses path compression to flatten the tree for better performance.
        """
        node = self.node_map[value]
        return self.find_set_node(node).value

    def find_set_node(self, node):
        """
        Helper method to find the root node of the set containing the given value.
        Applies path compression to optimize future queries.
        """
        if node.parent != node:
            # Recursively find the root and compress the path by making the parent point directly to the root
            node.parent = self.find_set_node(node.parent)

        return node.parent


class TestDisjointSet(unittest.TestCase):
    def test_disjoint_set(self):
        ds = DisjointSet()

        ds.make_set(1)
        ds.make_set(2)
        ds.make_set(3)
        ds.make_set(4)
        ds.make_set(5)
        ds.make_set(6)
        ds.make_set(7)

        ds.union(1, 2)
        ds.union(2, 3)
        ds.union(4, 5)
        ds.union(6, 7)
        ds.union(5, 6)
        ds.union(3, 7)

        self.assertTrue(
            ds.find_set(1)
            == ds.find_set(2)
            == ds.find_set(3)
            == ds.find_set(4)
            == ds.find_set(5)
            == ds.find_set(6)
            == ds.find_set(7)
            == 4
        )


if __name__ == "__main__":
    unittest.main()
