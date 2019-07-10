# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

"""
Example 1:

                3
               / \
              9  20
                 / \
                15  7


Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
             1
           /    \
          2      3
         /  \   / \
        4    5 6   7
 
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


Approach: Level Order Traversal + HM
queue = [1
hm = {dist: nodes}

pop -> 1 (dist = 0)
queue = [3, 2
hm = {0: 1}

pop -> 2 (dist = -1)
queue = [5, 4, 3
hm = {0: 1, -1: 2}

pop -> 3 (dist = 1)
queue = [7, 6, 5, 4
hm = {0: 1, -1: 2, 1: 3}

pop -> 4 (dist = -2)
queue = [7, 6, 5
hm = {0: 1, -1: 2, 1: 3, -2: 4}

pop -> 5 (dist = 0)
queue = [7, 6
hm = {0: [1, 5], -1: 2, 1: 3, -2: 4}

pop -> 6 (dist = 0)
queue = [7
hm = {0: [1, 5, 6], -1: 2, 1: 3, -2: 4}

pop -> 7 (dist = 2)
queue = [
hm = {0: [1, 5, 6], -1: 2, 1: 3, -2: 4, 2: 7}
"""

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
from collections import defaultdict
def vertical_order_traversal(root):
    if not root: return []
    dq = deque([[root, 0]])
    hm = defaultdict(list)

    while dq:
        node, dist = dq.pop()
        hm[dist].append(node.val)

        if node.left: dq.appendleft([node.left, dist - 1])
        if node.right: dq.appendleft([node.right, dist + 1])

    result = []
    for key in sorted(hm.keys()): result.append(hm[key])
    return result

import unittest
class TestVerticalOrderTraversal(unittest.TestCase):
    """
             1
           /    \
          2      3
         /  \   / \
        4    5 6   7

    """
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode (6)
    root.right.right = BinaryTreeNode(7)

    def test_vertical_order_traversal_invalid_input(self):
        self.assertEqual(vertical_order_traversal(None), [])
    
    def test_vertical_order_traversal_generic(self):
        self.assertEqual(vertical_order_traversal(self.root), [[4],[2],[1,5,6],[3],[7]])

if __name__ == "__main__": unittest.main()