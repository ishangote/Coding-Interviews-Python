import unittest
import sys


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_helper(node, prev, min_diff):
    if not node:
        return

    inorder_helper(node.left, prev, min_diff)

    if prev[0]:
        min_diff[0] = min(min_diff[0], node.value - prev[0].value)

    prev[0] = node

    inorder_helper(node.right, prev, min_diff)


# Time: O(n), where n => number of nodes in BT
# Space: O(n), implied call stack memory
def minimum_absolute_difference(root):
    prev = [None]
    min_diff = [sys.maxsize]

    inorder_helper(root, prev, min_diff)

    return min_diff[0]


class TestMinimumAbsoluteDifference(unittest.TestCase):
    def test_minimum_absolute_difference(self):

        root = BTNode(20)

        root.left = BTNode(15)
        root.right = BTNode(25)

        root.left.left = BTNode(7)
        root.left.right = BTNode(17)
        root.right.left = BTNode(24)

        self.assertEqual(minimum_absolute_difference(root), 1)


if __name__ == "__main__":
    unittest.main()
