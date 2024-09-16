class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def recursive_helper(node):
    if not node or (not node.left and not node.right): return
    node.left, node.right = node.right, node.left
    recursive_helper(node.left)
    recursive_helper(node.right)

# Time: O(n), n => number of nodes in the BT
# Space: O(n), implied memory
def invert_binary_tree(root):
    recursive_helper(root)
    return root

import unittest
class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        # Input
        root = BTNode(4)
        root.left = BTNode(2)
        root.right = BTNode(7)
        root.left.left = BTNode(1)
        root.left.right = BTNode(3)

        # Invert the binary tree
        invert_binary_tree(root)

        # Assertions
        self.assertEqual(root.value, 4)
        self.assertEqual(root.left.value, 7)
        self.assertEqual(root.right.value, 2)
        self.assertEqual(root.right.left.value, 3)
        self.assertEqual(root.right.right.value, 1)

if __name__ == "__main__": unittest.main()
