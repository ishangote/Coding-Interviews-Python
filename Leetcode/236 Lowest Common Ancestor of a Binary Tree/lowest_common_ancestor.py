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

    if not left and not right:
        return None

    if left and right:
        return root

    return left or right


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


if __name__ == "__main__":
    unittest.main()
