# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# Note: The length of path between two nodes is represented by the number of edges between them.

"""
Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

    1 -> 0

    1
   2   -> 1

    1    -> 2
  2   3

    1    -> 3   => left_height = 2 right_height = 1
  2   3
4

         1    -> 5 => left_height = 2 right_height = 3
     2      3
   4   5       6
            7

ans = left_height + right_height
"""
def height(root, ans): 
    if not root: return 0

    left_height = height(root.left, ans)
    right_height = height(root.right, ans)

    ans[0] = max(ans[0], 1 + left_height + right_height)
    return 1 + max(left_height, right_height)
  
def diameter(root):
    if not root: return 0
    ans = [0]
    height_of_tree = height(root, ans)  
    return ans[0] - 1

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import unittest
class TestDiameterOfBinaryTree(unittest.TestCase):
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.right.left = BTNode(5)
    root.right.left.right = BTNode(6)

    """
            1
        2        3
    4          5
                 6
    """

    def test_genric(self):
        self.assertEqual(diameter(self.root), 5)

if __name__ == "__main__": unittest.main()