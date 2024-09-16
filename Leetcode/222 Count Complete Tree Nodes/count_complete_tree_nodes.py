class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def calculate_height(node, direction):
    if not node: return 0
    return 1 + calculate_height(node.left, direction) if direction == "LEFT" else 1 + calculate_height(node.right, direction)

# Time: O(logn * logn)
# Space: O(logn * logn)
def count_nodes(root):
    if not root: return 0

    left_height = calculate_height(root, "LEFT")
    right_height = calculate_height(root, "RIGHT")

    if left_height == right_height: return (2 ** left_height) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)

import unittest
class TestCountCompleteTreeNodes(unittest.TestCase):
    def test_count_complete_tree_nodes(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)

        self.assertEqual(count_nodes(root), 4)

if __name__ == "__main__": unittest.main()
