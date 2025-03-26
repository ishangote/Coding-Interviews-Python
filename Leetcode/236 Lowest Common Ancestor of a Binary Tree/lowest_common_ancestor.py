import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n), where n => number of nodes in BT
# Space: O(h) ~ O(n) where h => height of BT
def lowest_common_ancestor(root, node1, node2):
    if not root:
        return None

    if root == node1 or root == node2:
        return root

    left = lowest_common_ancestor(root.left, node1, node2)
    right = lowest_common_ancestor(root.right, node1, node2)

    if left and right:
        return root

    return left or right


# ------------------------------------------------------------------------------------ #


class NTNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# * Variation: N-Ary Tree
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree (worst-case O(n))
def lowest_common_ancestor_nary_tree(root, node1, node2):
    if not root:
        return None

    if root == node1 or root == node2:
        return root

    found_nodes_count = 0
    found_node = None
    for child in root.children:
        candidate = lowest_common_ancestor_nary_tree(child, node1, node2)
        if candidate:
            found_nodes_count += 1
            found_node = candidate

    if found_nodes_count == 1:
        return found_node

    if found_nodes_count == 2:
        return root

    return None


# ------------------------------------------------------------------------------------ #


class TestLowestCommonAncestor(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(lowest_common_ancestor(None, BTNode(3), BTNode(6)), None)

    def test_nodes_not_found(self):
        root = BTNode(3)
        root.left = BTNode(6)
        root.right = BTNode(8)
        root.left.left = BTNode(2)
        root.left.right = BTNode(11)
        root.left.right.left = BTNode(9)
        root.left.right.right = BTNode(5)
        root.right.right = BTNode(13)
        root.right.right.left = BTNode(7)

        self.assertEqual(lowest_common_ancestor(root, BTNode(15), BTNode(18)), None)

    def test_lowest_common_ancestor_case1(self):
        root = BTNode(3)
        root.left = BTNode(6)
        root.right = BTNode(8)
        node1 = root.left.left = BTNode(2)
        root.left.right = BTNode(11)
        root.right.right = BTNode(13)
        root.left.right.left = BTNode(9)
        node2 = root.left.right.right = BTNode(5)
        root.right.right.left = BTNode(7)

        self.assertEqual(lowest_common_ancestor(root, node1, node2).value, 6)

    def test_lowest_common_ancestor_case2(self):
        root = BTNode(3)
        root.left = BTNode(6)
        node1 = root.right = BTNode(8)
        root.left.left = BTNode(2)
        node2 = root.left.right = BTNode(11)
        root.right.right = BTNode(13)
        root.left.right.left = BTNode(9)
        root.left.right.right = BTNode(5)
        root.right.right.left = BTNode(7)

        self.assertEqual(lowest_common_ancestor(root, node1, node2).value, 3)

    def test_lowest_common_ancestor_case3(self):
        root = BTNode(3)
        root.left = BTNode(6)
        node1 = root.right = BTNode(8)
        root.left.left = BTNode(2)
        root.left.right = BTNode(11)
        root.right.right = BTNode(13)
        root.left.right.left = BTNode(9)
        root.left.right.right = BTNode(5)
        node2 = root.right.right.left = BTNode(7)

        self.assertEqual(lowest_common_ancestor(root, node1, node2).value, 8)


# Unit tests for the lowest_common_ancestor_nary_tree function
class TestLowestCommonAncestorNaryTree(unittest.TestCase):
    def setUp(self):
        # Create an N-ary tree:
        #         A
        #       / | \
        #      B  C  D
        #     / \    |
        #    E   F   G
        #           /|\
        #          H I J
        self.nodeA = NTNode("A")
        self.nodeB = NTNode("B")
        self.nodeC = NTNode("C")
        self.nodeD = NTNode("D")
        self.nodeE = NTNode("E")
        self.nodeF = NTNode("F")
        self.nodeG = NTNode("G")
        self.nodeH = NTNode("H")
        self.nodeI = NTNode("I")
        self.nodeJ = NTNode("J")

        self.nodeA.children = [self.nodeB, self.nodeC, self.nodeD]
        self.nodeB.children = [self.nodeE, self.nodeF]
        self.nodeD.children = [self.nodeG]
        self.nodeG.children = [self.nodeH, self.nodeI, self.nodeJ]

    def test_lca_same_node(self):
        # LCA of the same node should be the node itself.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeE, self.nodeE),
            self.nodeE,
        )

    def test_lca_sibling_nodes(self):
        # LCA of siblings E and F should be their parent B.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeE, self.nodeF),
            self.nodeB,
        )

    def test_lca_different_subtrees(self):
        # LCA of E (under B) and C (direct child of A) should be A.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeE, self.nodeC),
            self.nodeA,
        )

    def test_lca_deep_nodes(self):
        # LCA of H and I (both under G) should be G.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeH, self.nodeI),
            self.nodeG,
        )

    def test_lca_cross_subtrees(self):
        # LCA of F (under B) and I (under G, which is under D) should be A.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeF, self.nodeI),
            self.nodeA,
        )

    def test_lca_node_not_present(self):
        # When one or both nodes are not in the tree.
        node_not_in_tree = NTNode("Z")
        # If one node is missing, the function will return the found node.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(self.nodeA, self.nodeE, node_not_in_tree),
            self.nodeE,
        )
        # If both nodes are missing, the function should return None.
        self.assertEqual(
            lowest_common_ancestor_nary_tree(
                self.nodeA, node_not_in_tree, node_not_in_tree
            ),
            None,
        )


if __name__ == "__main__":
    unittest.main()
