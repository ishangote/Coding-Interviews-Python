import unittest
import sys
from collections import defaultdict, deque


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# --------------------------------------------------------------- #


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


# --------------------------------------------------------------- #


# Time: O(k•(n/k)log(n/k)) ~ O(n•log(n/k)), where k => number of columns, n => number of nodes
# Space: O(n)
def vertical_order_traversal_optimized(root):
    if not root:
        return []

    queue = deque([(0, 0, root)])
    distance_map = defaultdict(list)
    min_column, max_column = sys.maxsize, -sys.maxsize

    while queue:
        col, row, node = queue.pop()
        distance_map[col].append((row, node.value))
        min_column = min(min_column, col)
        max_column = max(max_column, col)

        if node.left:
            queue.appendleft((col - 1, row + 1, node.left))

        if node.right:
            queue.appendleft((col + 1, row + 1, node.right))

    return [
        [value for _, value in sorted(distance_map[col])]
        for col in range(min_column, max_column + 1)
    ]


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

    def test_vertical_order_traversal_optimized(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)

        root.right.left = BTNode(6)
        root.right.right = BTNode(7)

        self.assertEqual(
            vertical_order_traversal_optimized(root), [[4], [2], [1, 5, 6], [3], [7]]
        )


if __name__ == "__main__":
    unittest.main()
