import unittest
from collections import defaultdict, deque


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n), n => number of nodes in BT
# Space: O(n), n => number of nodes in BT
def binary_tree_right_side_view_level_order(root):
    if not root:
        return []
    level_order = defaultdict(list)
    queue = deque([(root, 0)])
    max_level = 0

    while queue:
        node, level = queue.pop()
        max_level = max(max_level, level)
        level_order[level].append(node.value)

        if node.left:
            queue.appendleft((node.left, level + 1))
        if node.right:
            queue.appendleft((node.right, level + 1))

    return [level_order[level][-1] for level in range(0, max_level + 1)]


class TestBinaryTreeRightSideView(unittest.TestCase):
    def test_binary_tree_right_side_view_base_case(self):
        self.assertEqual(binary_tree_right_side_view_level_order(None), [])

    def test_binary_tree_right_side_view(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.left = BTNode(6)
        root.right.right = BTNode(7)

        root.left.right.left = BTNode(8)

        self.assertEqual(binary_tree_right_side_view_level_order(root), [1, 3, 7, 8])


if __name__ == "__main__":
    unittest.main()
