"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:

                1 ...> None
            /        \
           2.........>3...>None
          /  \      /   \
         4...>5..> 6 ...>7...>None


"""

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

#Level order traversal
from collections import deque
def populate_next_right(root):
    if not root: return None

    dq = deque([root])
    while dq:
      num_nodes = len(dq)
      next_node = None
      for itr in range(num_nodes):
        node = dq.pop()
        node.next = next_node
        next_node = node
        if node.right: dq.appendleft(node.right)
        if node.left: dq.appendleft(node.left)

import unittest
class TestPopulateNextRightPerfectBinaryTree(unittest.TestCase):
  root = BinaryTreeNode(1)
  root.left = BinaryTreeNode(2)
  root.right = BinaryTreeNode(3)
  root.left.left = BinaryTreeNode(4)
  root.left.right = BinaryTreeNode(5)
  root.right.left = BinaryTreeNode(6)
  root.right.right = BinaryTreeNode(7)

  def print_all_next_in_level_order(self):
    result = []
    if not self.root: return None
    dq = deque([self.root])
    while dq:
      node = dq.pop()
      if node.next: result.append(node.next.val)
      else: result.append(None)
      if node.left: dq.appendleft(node.left)
      if node.right: dq.appendleft(node.right)
      
    return result

  def test_populate_next_right(self):
    populate_next_right(self.root)
    result = self.print_all_next_in_level_order()
    self.assertEqual(result, [None, 3, None, 5, 6, 7, None])

if __name__ == "__main__": unittest.main()