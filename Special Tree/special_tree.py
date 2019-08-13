"""

A binary tree is univalued if every node in the tree has the same value. 
Return true if the given tree is univalued.

                  1
            1             1
        1      1      2       1

"""
import unittest
class SpecialTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_special_tree(root):
    if root == None: return True
    return dfs(root, root.val)
    
def dfs(node, val):
    if node == None: return True
    if node.val != val: return False
    return dfs(node.left, val) and dfs(node.right, val)

#-------------One function-------------#

def is_special_dfs(root):
    if not root: return True
    
    if root.right:
        if root.val != root.right.val: return False
        
    if root.left:
        if root.val != root.left.val: return False
    
    return is_special_dfs(root.right) and is_special_dfs(root.left)

#-------------TEST-------------#

class TestIsSpecialTree(unittest.TestCase):
    def test_root_none(self):
        self.assertEqual(is_special_tree(None), True)
        self.assertEqual(is_special_dfs(None), True)

    def test_no_left_root(self):
        a = SpecialTreeNode(1)
        b = SpecialTreeNode(1)
        a.right = b
        self.assertEqual(is_special_tree(a), True)
        self.assertEqual(is_special_dfs(a), True)
    
    def test_no_right_root(self):
        a = SpecialTreeNode(1)
        b = SpecialTreeNode(1)
        a.left = b
        self.assertEqual(is_special_tree(a), True)
        self.assertEqual(is_special_dfs(a), True)

    def test_special_tree(self):
        a = SpecialTreeNode(1)
        b = SpecialTreeNode(1)
        c = SpecialTreeNode(1)
        d = SpecialTreeNode(1)
        e = SpecialTreeNode(1)
        f = SpecialTreeNode(1)
        g = SpecialTreeNode(1)
        h = SpecialTreeNode(1)

        a.left = b
        a.right = c

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        e.left = h

        """
                       a
                b            c
            d       e      f   g
                   h
        """
        self.assertEqual(is_special_tree(a), True)
        self.assertEqual(is_special_dfs(a), True)


    def test_not_special_tree(self):
        a = SpecialTreeNode(1)
        b = SpecialTreeNode(1)
        c = SpecialTreeNode(1)
        d = SpecialTreeNode(1)
        e = SpecialTreeNode(1)
        f = SpecialTreeNode(1)
        g = SpecialTreeNode(1)
        h = SpecialTreeNode(2)

        a.left = b
        a.right = c

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        e.left = h

        self.assertEqual(is_special_tree(a), False)
        self.assertEqual(is_special_dfs(a), False)

    def test_root_value_different_node(self):
        a = SpecialTreeNode(2)
        b = SpecialTreeNode(1)
        c = SpecialTreeNode(1)
        d = SpecialTreeNode(1)
        e = SpecialTreeNode(1)
        f = SpecialTreeNode(1)
        g = SpecialTreeNode(1)
        h = SpecialTreeNode(1)

        a.left = b
        a.right = c

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        e.left = h

        self.assertEqual(is_special_tree(a), False)
        self.assertEqual(is_special_dfs(a), False)

if __name__ == '__main__': unittest.main()