# Problem 1:
"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
                                                        
# Problem 2: IMPORTANT TESTCASE: ROOT and only ONE CHILD NODE
"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if not root: return 0
    if not root.left and not root.right: return 1
    if not root.left and root.right: return 1 + max_depth(root.right)
    if root.left and not root.right: return 1 + max_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))

import unittest
class TestMinMaxDepthBinaryTree(unittest.TestCase):

    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)
    root1.right = BinaryTreeNode(3)
    root1.right.left = BinaryTreeNode(4)

    root2 = BinaryTreeNode(1)
    root2.left = BinaryTreeNode(2)

    def test_max_depth(self): self.assertEqual(max_depth(self.root1), 3)
    def test_min_depth(self): self.assertEqual(min_depth(self.root2), 2)

if __name__ == "__main__": unittest.main()