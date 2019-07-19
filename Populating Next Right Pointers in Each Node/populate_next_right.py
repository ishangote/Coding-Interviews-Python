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

              1
            /   \
           2     3
          / \   / \
         4   5 6   7


"""

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

from collections import deque
def populate_next_right(root):
    if not root: return None

    dq = deque([root])
    while dq:
        node = dq.pop()
        
