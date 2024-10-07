import unittest


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def recursive_helper(node):
    if not node:
        return (0, 0)

    (left_sum, left_sum_tilt) = recursive_helper(node.left)
    (right_sum, right_sum_tilt) = recursive_helper(node.right)

    return (
        left_sum + right_sum + node.value,
        left_sum_tilt + right_sum_tilt + abs(left_sum - right_sum),
    )


# Time: O(n), where n => number of nodes in BT
# Space: O(n), implicit call stack memory for recursion
def binary_tree_tilt(root):
    return recursive_helper(root)[1]


class TestBinaryTreeTilt(unittest.TestCase):

    def test_edge_binary_tree_tilt(self):
        self.assertEqual(binary_tree_tilt(None), 0)
        self.assertEqual(binary_tree_tilt(BTNode(2)), 0)

    def test_binary_tree_tilt(self):
        root = BTNode(4)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(1)
        root.right.left = BTNode(2)

        self.assertEqual(binary_tree_tilt(root), 5)


if __name__ == "__main__":
    unittest.main()
