import unittest
from collections import defaultdict


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, row, col, nodes):
    if not node:
        return

    nodes.append((col, row, node.value))

    recursive_helper(node.left, row + 1, col - 1, nodes)
    recursive_helper(node.right, row + 1, col + 1, nodes)


# Time: O(nlogn), where n => number of nodes in BT
# Space: O(n)
def vertical_order_traversal(root):
    nodes = []

    recursive_helper(root, 0, 0, nodes)

    # Sort by col, then row, then value
    nodes.sort()

    res = defaultdict(list)
    for col, row, value in nodes:
        res[col].append(value)

    # Python dictionary maintains insertion order
    return list(res.values())


class TestVerticalOrderTraversal(unittest.TestCase):
    def test_vertical_order_traversal(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)

        root.right.left = BTNode(6)
        root.right.right = BTNode(7)

        self.assertEqual(
            vertical_order_traversal(root), [[4], [2], [1, 5, 6], [3], [7]]
        )


if __name__ == "__main__":
    unittest.main()
