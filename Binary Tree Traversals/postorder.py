# Given a binary tree, return the POSTORDER traversal of its nodes’ values. Using recursion is not allowed.
# Inorder: left -> root -> right
# Preorder: root -> left -> right
# Postorder: left -> right -> root

"""
Postorder: left -> right -> root

        1
      /   \
     2     3
    / \
   4   5
        \
         6

4 5 6 2 3 1

Approach 1: Two Stacks: Pop from stack1 and put in stack2 and left, right in stack 1

stack1 = [1]
stack2 = []

stack1 = [3 ,2]
stack2 = [1]

stack1 = [2]
stack2 = [3, 1]

stack1 = [2]
stack2 = [3, 1]

stack1 = [5, 4]
stack2 = [2, 3, 1]

stack1 = [6, 4]
stack2 = [5, 2, 3, 1]

stack1 = [4]
stack2 = [6, 5, 2, 3, 1]

stack1 = []
stack2 = [4, 6, 5, 2, 3, 1]
"""

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_two_stacks(root):
    if not root: return None
    stack1, stack2 = [], []
    stack1.append(root)

    while stack1:
        node = stack1.pop()
        if node.left: stack1.append(node.left)
        if node.right: stack1.append(node.right)
        stack2.append(node.val)

    return stack2[::-1]        

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
        self.assertEqual(postorder_two_stacks(None), None)

    def test_inorder_binary_tree(self):
        self.assertEqual(postorder_two_stacks(self.root), [5, 6, 0, 11, -10, 10])
        
if __name__ == "__main__": unittest.main()