# Given a binary tree, return the INORDER traversal of its nodes’ values. Using recursion is not allowed.
# Inorder: left -> root -> right
# Preorder: root -> left -> right
# Postorder: left -> right -> root
"""
Example :
Given binary tree
   1
    \
     2
    /
   3
return [1,3,2]

        1
      /   \
     2     3
    / \
   4  5

stack = [1, 2, 4] []
stack = [1, 2, 5] [4]

"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_iterative(root):
    stack, result = [], []

    while True:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            if not stack: break
            root = stack.pop()
            result.append(root.val)
            root = root.right

    return result

import unittest
class TestInorderTraversalBinaryTree(unittest.TestCase):

    """
        10
       /  \
      0    -10
     / \     \
    5   6     11
    """

    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(0)
    root.left.left = BinaryTreeNode(5)
    root.left.right = BinaryTreeNode(6)
    root.right = BinaryTreeNode(-10)
    root.right.right = BinaryTreeNode(11)

    def test_inorder_binary_tree_invalid_input(self):
        self.assertEqual(inorder_iterative(None), [])

    def test_inorder_binary_tree(self):
        self.assertEqual(inorder_iterative(self.root), [5, 0, 6, 10, -10, 11])

if __name__ == "__main__": unittest.main()