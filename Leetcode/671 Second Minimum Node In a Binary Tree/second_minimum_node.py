import sys
from typing import Final
import unittest


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def recursive_helper(node, res, MINIMUM):
    if MINIMUM < node.value < res[0]:
        res[0] = node.value

    if node.left:
        recursive_helper(node.left, res, MINIMUM)

    if node.right:
        recursive_helper(node.right, res, MINIMUM)


# Time: O(n), where n => number of nodes in BT
# Space: O(n), implicit call stack memory
def second_minimum_node(root):
    res = [sys.maxsize]
    MINIMUM: Final[int] = root.value

    recursive_helper(root, res, MINIMUM)

    return res[0] if res[0] != sys.maxsize else -1


class TestSecondMinimumNode(unittest.TestCase):
    def test_second_minimum_node_edge(self):
        self.assertEqual(second_minimum_node(BTNode(2)), -1)

        root = BTNode(2)
        root.left = BTNode(2)
        root.right = BTNode(2)

        self.assertEqual(second_minimum_node(root), -1)

    def test_second_minimum_node(self):
        root = BTNode(5)

        root.left = BTNode(7)
        root.right = BTNode(5)

        root.right.left = BTNode(5)
        root.right.right = BTNode(6)

        self.assertEqual(second_minimum_node(root), 6)


if __name__ == "__main__":
    unittest.main()
