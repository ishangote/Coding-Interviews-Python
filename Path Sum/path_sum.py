# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Note: A leaf is a node with no children.
"""
Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Approach 1: Recursion

for each node recursively check if total_sum-root_val == 0: if yes return true else: check for left sub_tree OR right sub_tree

Approach 2: Iteratively by building a stack whih contains current root and the current target

"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_sum(root, target):
    if not root: return False
    
    #If reached leaf node
    target -= root.val
    if not root.left and not root.right: return target == 0
    return path_sum(root.left, target) or path_sum(root.right, target)

def path_sum_iterative(root, target):
    if not root: return False
    stack = [(root, target - root.val)]
    while stack:
        curr_node, curr_target = stack.pop()
        if not curr_node.left and not curr_node.right and curr_target == 0: return True
        
        if curr_node.right: stack.append((curr_node.right, curr_target - curr_node.right.val))
        if curr_node.left: stack.append((curr_node.left, curr_target - curr_node.left.val))
        
    return False

import unittest
class TestPathSum(unittest.TestCase):
    root = BinaryTreeNode(5) 
    root.left = BinaryTreeNode(4) 
    root.right = BinaryTreeNode(8) 
    root.left.left = BinaryTreeNode(11) 
    root.right.left = BinaryTreeNode(13)  
    root.right.right = BinaryTreeNode(4)
    root.left.left.left = BinaryTreeNode(7)
    root.left.left.right = BinaryTreeNode(2)
    root.right.right.right = BinaryTreeNode(1)

    #-----------------------------------------
    
    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)

    def test_path_sum(self):
        self.assertEqual(path_sum(self.root, 22), True)
        self.assertEqual(path_sum_iterative(self.root, 22), True)

        self.assertEqual(path_sum(self.root1, 2), False)
        self.assertEqual(path_sum_iterative(self.root1, 2), False)
if __name__ == "__main__": unittest.main()