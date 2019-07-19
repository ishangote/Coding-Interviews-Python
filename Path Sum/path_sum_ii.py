# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
"""
Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_sum_ii_iterative(root, target):
    if not root: return []

    result = []
    stack = [(root, target - root.val, [root.val])]
    while stack:
        curr_node, curr_target, curr_path = stack.pop()
        if not curr_node.left and not curr_node.right and curr_target == 0: 
            result.append(curr_path)
            
        if curr_node.right: stack.append((curr_node.right, curr_target - curr_node.right.val, curr_path + [curr_node.right.val]))
        if curr_node.left: stack.append((curr_node.left, curr_target - curr_node.left.val, curr_path + [curr_node.left.val]))
    
    return result

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
    root.right.right.left = BinaryTreeNode(5)
    root.right.right.right = BinaryTreeNode(1)

    def test_path_sum_ii(self):
        self.assertEqual(path_sum_ii_iterative(self.root, 22), [[5, 4, 11, 2],[5, 8, 4, 5]])

if __name__ == "__main__": unittest.main()