"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#-------------------------------------------------------------

def symm_tree_recursive(root):
    if not root: return True
    return symm_tree_util(root.left, root.right)

def symm_tree_util(node1, node2):
    if not node1 and not node2: return True
    if not node1 or not node2: return False
    if node1.val != node2.val: return False
    
    return symm_tree_util(node1.left, node2.right) and symm_tree_util(node1.right, node2.left)

#-------------------------------------------------------------

def symm_tree_iter(root):
    if not root: return True

    stack = [(root.left, root.right)]
    while stack:
        left_node, right_node = stack.pop()
        
        # Both None
        #The continue statement in Python returns the control to the beginning of the current loop. 
        #When encountered, the loop starts next iteration without executing the remaining statements in the current iteration.
        if not left_node and not right_node: continue
            
        #One of the nodes is None
        if not left_node or not right_node: return False
        
        if left_node.val != right_node.val: return False

        stack.append((left_node.left, right_node.right))
        stack.append((left_node.right, right_node.left))

    return True

#-------------------------------------------------------------

import unittest
class TestSymmTree(unittest.TestCase):
    def test_root_none(self):
        self.assertEqual(symm_tree_recursive(None), True)
        self.assertEqual(symm_tree_iter(None), True)

    def test_symm_tree_true(self):
        root1 = BinaryTreeNode(1)
        root1.left = BinaryTreeNode(2)
        root1.right = BinaryTreeNode(2)
        root1.left.left = BinaryTreeNode(3)
        root1.left.right = BinaryTreeNode(4)
        root1.right.left = BinaryTreeNode(4)
        root1.right.right = BinaryTreeNode(3)

        self.assertEqual(symm_tree_recursive(root1), True)
        self.assertEqual(symm_tree_iter(root1), True)

    def test_symm_tree_false(self):
        root2 = BinaryTreeNode(1)
        root2.left = BinaryTreeNode(2)
        root2.right = BinaryTreeNode(2)
        root2.right.right = BinaryTreeNode(3)
        root2.left.right = BinaryTreeNode(3)

        self.assertEqual(symm_tree_recursive(root2), False)
        self.assertEqual(symm_tree_iter(root2), False)

if __name__ == "__main__":  unittest.main()