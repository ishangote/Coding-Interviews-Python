import unittest
from collections import defaultdict, deque


class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


# ------------------------------------------------------------------------ #
# * Variation: Left and Right Side View Clockwise

"""
Input:
            3
L->     2       4       <- R
    1         8
      9

Left (from bottom to up) [9, 1, 2, 3]
Right (from top to bottom) [3, 4, 8, 9]

* Constraint: Include the root node only once. Rest can be counted as part of both views.
                   
Output = [9, 1, 2, 3, 4, 8, 9]
                   ^
                   root.value

level_order =
{
    0: [3]
    1: [2, 4]
    2: [1, 8]
    3: [9]
}
"""


def binary_tree_left_right_side_view(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    level_order = defaultdict(list)
    max_level = 0
    res = []

    while queue:
        node, level = queue.pop()
        level_order[level].append(node.value)
        max_level = max(max_level, level)

        if node.left:
            queue.appendleft((node.left, level + 1))

        if node.right:
            queue.appendleft((node.right, level + 1))

    for level in range(max_level, -1, -1):
        res.append(level_order[level][0])

    for level in range(1, max_level + 1):
        res.append(level_order[level][-1])

    return res


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


class TestBinaryTreeLeftRightSideView(unittest.TestCase):
    def test_given_example(self):
        """
        Construct the following tree:
                    3
                  /   \
                 2     4
                /       \
               1         8
                \
                 9

        Expected level order (as processed):
            Level 0: [3]
            Level 1: [2, 4]
            Level 2: [1, 8]
            Level 3: [9]

        Left view (bottom-up): [9, 1, 2, 3]
        Right view (top-down, skipping root): [4, 8, 9]
        Combined output: [9, 1, 2, 3, 4, 8, 9]
        """
        node9 = BTNode(9)
        node1 = BTNode(1, None, node9)
        node2 = BTNode(2, node1, None)
        node8 = BTNode(8)
        node4 = BTNode(4, node8, None)
        node3 = BTNode(3, node2, node4)

        expected = [9, 1, 2, 3, 4, 8, 9]
        self.assertEqual(binary_tree_left_right_side_view(node3), expected)

    def test_single_node(self):
        node = BTNode(5)
        # For a single node tree, left view is [5] and no additional right view.
        self.assertEqual(binary_tree_left_right_side_view(node), [5])

    def test_left_skewed_tree(self):
        # Construct a left-skewed tree:
        #       1
        #      /
        #     2
        #    /
        #   3
        node3 = BTNode(3)
        node2 = BTNode(2, node3)
        node1 = BTNode(1, node2)
        # Level order:
        # Level 0: [1]
        # Level 1: [2]
        # Level 2: [3]
        # Left view (bottom-up): [3, 2, 1]
        # Right view (levels 1 and 2): [2, 3]
        # Combined: [3, 2, 1, 2, 3]
        expected = [3, 2, 1, 2, 3]
        self.assertEqual(binary_tree_left_right_side_view(node1), expected)

    def test_right_skewed_tree(self):
        # Construct a right-skewed tree:
        # 1
        #  \
        #   2
        #    \
        #     3
        node3 = BTNode(3)
        node2 = BTNode(2, None, node3)
        node1 = BTNode(1, None, node2)
        # Level order:
        # Level 0: [1]
        # Level 1: [2]
        # Level 2: [3]
        # Left view (bottom-up): [3, 2, 1]
        # Right view (levels 1 and 2): [2, 3]
        # Combined: [3, 2, 1, 2, 3]
        expected = [3, 2, 1, 2, 3]
        self.assertEqual(binary_tree_left_right_side_view(node1), expected)

    def test_empty_tree(self):
        # If the tree is empty, we expect an empty list.
        self.assertEqual(binary_tree_left_right_side_view(None), [])


if __name__ == "__main__":
    unittest.main()
