# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

"""
Example:
Input: [1,2,3]
       1   <-
      / \
     2   3

Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Approach 1: DFS + STACK: Traverse multiple times till we reach leaf nodes and store all paths on the way
stack = [4]
curr_path = [4]
while stack not empty: 
  check if node is leaf if yes add curr_path to paths
"""

class BinaryTreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def sum_root_to_leaf_numbers(root):
  if not root: return 0
  stack  = [(root, root.val)]
  result = 0
  while stack:
    node, node_val = stack.pop()
    # Condition to check if current node is leaf node:
    if not node.left and not node.right: result += node_val
    if node.right: stack.append((node.right, node_val * 10 + node.right.val))
    if node.left: stack.append((node.left, node_val*10 + node.left.val))
  return result

import unittest
class TestSumRootToLeafNumbers(unittest.TestCase):

  root = BinaryTreeNode(4)
  root.left = BinaryTreeNode(9)
  root.left.left = BinaryTreeNode(5)
  root.left.right = BinaryTreeNode(1)
  root.right = BinaryTreeNode(0)

  root1 = BinaryTreeNode(1)
  root1.left = BinaryTreeNode(2)
  root1.right = BinaryTreeNode(3)

  def test_invalid_input(self):
    self.assertEqual(sum_root_to_leaf_numbers(None), 0)
  
  def test_one_node(self):
    self.assertEqual(sum_root_to_leaf_numbers(BinaryTreeNode(1)), 1)
  
  def test_generic_input(self):
    self.assertEqual(sum_root_to_leaf_numbers(self.root), 1026)
    self.assertEqual(sum_root_to_leaf_numbers(self.root1), 25)
if __name__ == "__main__": unittest.main()