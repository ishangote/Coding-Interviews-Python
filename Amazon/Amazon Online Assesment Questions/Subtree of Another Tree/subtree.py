"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_subtree(s, t):
    if not t: return True
    if not s: return False
    if is_identical_trees(s, t): return True

    return is_subtree(s.left, t) or is_subtree(s.right, t)

def is_identical_trees(root1, root2):
    if not root1 and not root2: return True
    if root1 and root2:
        if root1.val == root2.val and is_identical_trees(root1.left, root2.left) and is_identical_trees(root1.right, root2.right): return True
    
    return False

import unittest
class TestSubtreeOfAnotherTree(unittest.TestCase):
    def test_edge_cases(self):
        s, t = None, BinaryTreeNode(1)
        self.assertEqual(is_subtree(s, t), False)
        t, s = None, BinaryTreeNode(1)
        self.assertEqual(is_subtree(s, t), True)

    def test_generic(self):
        s = BinaryTreeNode(3)
        s.left = BinaryTreeNode(4)
        s.right = BinaryTreeNode(5)
        s.left.left = BinaryTreeNode(1)
        s.left.right = BinaryTreeNode(2)
        s.left.right.left = BinaryTreeNode(0)

        t = BinaryTreeNode(4)
        t.left = BinaryTreeNode(1)
        t.right = BinaryTreeNode(2)

        self.assertEqual(is_subtree(s, t), False)

        s = BinaryTreeNode(3)
        s.left = BinaryTreeNode(4)
        s.right = BinaryTreeNode(5)
        s.left.left = BinaryTreeNode(1)
        s.left.right = BinaryTreeNode(2)
        # s.left.right.left = BinaryTreeNode(0)

        self.assertEqual(is_subtree(s, t), True)

if __name__ == "__main__": unittest.main()