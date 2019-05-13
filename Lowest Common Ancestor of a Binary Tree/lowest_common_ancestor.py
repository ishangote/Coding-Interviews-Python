"""
Lowest Common Ancestor Binary Tree

               3
            /     \
           6       8
         /  \        \
        2   11        13
           /  \       /
          9    5     7 
            
"""

import unittest
class BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, node1, node2):
    if root == None: return None
    if root.data == node1 or root.data == node2: return root
    
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left == None and right == None: return None
    if left != None and right != None: return root

    return left if left != None else right

#TESTING...

class TestLowestCommonAncestor(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(lca(None, 3, 6), None)

    def test_nodes_not_found(self):
        #Construct Binary Tree
        root = BinTreeNode(3)
        root.left = BinTreeNode(6)
        root.right = BinTreeNode(8)
        root.left.left = BinTreeNode(2)
        root.left.right = BinTreeNode(11)
        root.left.right.left = BinTreeNode(9)
        root.left.right.right = BinTreeNode(5)
        root.right.right = BinTreeNode(13)
        root.right.right.left = BinTreeNode(7)

        self.assertEqual(lca(root, 15, 18), None)

    def test_lca(self):
        #Construct Binary Tree
        root = BinTreeNode(3)
        root.left = BinTreeNode(6)
        root.right = BinTreeNode(8)
        root.left.left = BinTreeNode(2)
        root.left.right = BinTreeNode(11)
        root.left.right.left = BinTreeNode(9)
        root.left.right.right = BinTreeNode(5)
        root.right.right = BinTreeNode(13)
        root.right.right.left = BinTreeNode(7)
        
        self.assertEqual(lca(root, 2, 8).data, 3)
        self.assertEqual(lca(root, 9, 5).data, 11)
        self.assertEqual(lca(root, 8, 7).data, 8)
        self.assertEqual(lca(root, 9, 3).data, 3)
        self.assertEqual(lca(root, 2, 5).data, 6)

if __name__ == "__main__": unittest.main()