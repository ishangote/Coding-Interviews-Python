# Given a binary tree, return the PREORDER traversal of its nodes’ values. Using recursion is not allowed.
# Inorder: left -> root -> right
# Preorder: root -> left -> right
# Postorder: left -> right -> root

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if not root: return None
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result

import unittest
class TestPreorderTraversalBinaryTree(unittest.TestCase):
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
        self.assertEqual(preorder(None), None)

    def test_inorder_binary_tree(self):
        self.assertEqual(preorder(self.root), [10, 0, 5, 6, -10, 11])
        
if __name__ == "__main__": unittest.main()