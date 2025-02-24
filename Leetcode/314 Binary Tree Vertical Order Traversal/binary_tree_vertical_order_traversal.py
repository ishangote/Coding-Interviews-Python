import unittest
from collections import deque
from collections import defaultdict


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(nlogn), where n => number of nodes in tree
# Space: O(n)
def binary_tree_vertical_order_traversal(root):
    if not root:
        return []

    queue = deque([(0, root)])
    distance_map = defaultdict(list)

    while queue:
        dist, node = queue.pop()
        distance_map[dist].append(node.value)
        if node.left:
            queue.appendleft((dist - 1, node.left))
        if node.right:
            queue.appendleft((dist + 1, node.right))

    return [distance_map[dist] for dist in sorted(distance_map.keys())]


# Time: O(n), where n => number of nodes in BT
# Space: O(n)
def binary_tree_vertical_order_traversal_optimized(root):
    if not root:
        return []

    queue = deque([(0, root)])
    distance_map = defaultdict(list)
    min_column, max_column = 0, 0

    while queue:
        dist, node = queue.pop()

        min_column = min(min_column, dist)
        max_column = max(max_column, dist)

        distance_map[dist].append(node.value)

        if node.left:
            queue.appendleft((dist - 1, node.left))
        if node.right:
            queue.appendleft((dist + 1, node.right))

    return [distance_map[dist] for dist in range(min_column, max_column + 1)]


class TestBinaryTreeVerticalOrderTraversal(unittest.TestCase):
    def test_binary_tree_vertical_order_traversal(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(10)
        root.right.left = BTNode(9)
        root.right.right = BTNode(11)

        root.left.left.right = BTNode(5)
        root.left.left.right.right = BTNode(6)

        self.assertListEqual(
            binary_tree_vertical_order_traversal(root),
            [[4], [2, 5], [1, 10, 9, 6], [3], [11]],
        )

    def test_binary_tree_vertical_order_traversal_optimized(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(10)
        root.right.left = BTNode(9)
        root.right.right = BTNode(11)

        root.left.left.right = BTNode(5)
        root.left.left.right.right = BTNode(6)

        self.assertListEqual(
            binary_tree_vertical_order_traversal_optimized(root),
            [[4], [2, 5], [1, 10, 9, 6], [3], [11]],
        )


if __name__ == "__main__":
    unittest.main()
