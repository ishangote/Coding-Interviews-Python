import unittest
from node_depth_iterative import node_depth_iterative
from node_depth_recursive import node_depth_recursive

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
            1
        2       3
    4     5  6      7
  8   9
"""

class TestNodeDepths(unittest.TestCase):
    def test_generic(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right = BinaryTree(5)
        root.left.left.right = BinaryTree(9)
        root.right = BinaryTree(3)
        root.right.right = BinaryTree(7)
        root.right.left = BinaryTree(6)

        self.assertEqual(node_depth_iterative(root), 16)
        self.assertEqual(node_depth_recursive(root), 16)
        
if __name__ == "__main__": unittest.main()