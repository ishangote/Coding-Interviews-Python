"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


            6
        2       8
       0  4   7   9
         3 5

Cases:
1. p, q both in left subtree
2. p, q both in right subtree
3. p, q in different subtrees



Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def lca_bst_recursive(root, p, q):
    if p.val > root.val and q.val > root.val: 
        return lca_bst_recursive(root.right, p, q)
    elif p.val < root.val and q.val < root.val: 
        return lca_bst_recursive(root.left, p, q)
    else: return root

def lca_bst_iterative(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val: root = root.right
        elif p.val < root.val and q.val < root.val: root = root.left
        else: return root

import unittest
class TestLowestCommonAncestor(unittest.TestCase):
    root = BSTNode(6)
    root.left = BSTNode(2)
    root.right = BSTNode(8)
    root.left.left = BSTNode(0)
    root.left.right = BSTNode(4)
    root.left.right.left = BSTNode(3)
    root.left.right.right = BSTNode(5)
    root.right.left = BSTNode(7)
    root.right.right = BSTNode(9)

    def test_recursive_generic(self):
        p, q = self.root.left, self.root.left.right.left
        self.assertEqual(lca_bst_recursive(self.root, p, q).val, 2)

        p, q = self.root.right.left, self.root.right
        self.assertEqual(lca_bst_recursive(self.root, p, q).val, 8)

        p, q = self.root.left.right.left, self.root.right.left
        self.assertEqual(lca_bst_recursive(self.root, p, q).val, 6)

    def test_iterative_generic(self):
        p, q = self.root.left, self.root.left.right.left
        self.assertEqual(lca_bst_iterative(self.root, p, q).val, 2)

        p, q = self.root.right.left, self.root.right
        self.assertEqual(lca_bst_iterative(self.root, p, q).val, 8)

        p, q = self.root.left.right.left, self.root.right.left
        self.assertEqual(lca_bst_iterative(self.root, p, q).val, 6)

if __name__ == "__main__": unittest.main()