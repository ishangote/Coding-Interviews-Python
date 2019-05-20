# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

"""
Example:
Given binary tree [3,9,20,null,null,15,7],

    3   <
   / \
  9  20
    /  \
   15   7

DFS
H(3) = 1 + max(H(9), H(20))
     = 1 + max(1 + max(H(None), H(None)), 1+ max(H(15), H(7)))
     = ...
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if not root: return 0
    else: return 1 + max(max_depth(root.left), max_depth(root.right))

import unittest
class TestMaxDepthBinaryTree(unittest.TestCase):
    def test_none_root(self):
        self.assertEqual(max_depth(None), 0)

    def test_root(self):
        self.assertEqual(max_depth(BinaryTreeNode(3)), 1)

    def test_max_depth(self):
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(9)
        root.right = BinaryTreeNode(20)
        root.right.left = BinaryTreeNode(15)
        root.right.right = BinaryTreeNode(7)

        self.assertEqual(max_depth(root), 3)

if __name__ == "__main__": unittest.main()