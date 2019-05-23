# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

"""
For example:
Given binary tree,


                          1     
                        /   \
                       2     3   
                      / \   / \
                     4   5 6   7
                    /   /       \
                   8   9         10


return its zigzag level order traversal as: [[1], [3, 2], [4, 5, 6, 7], [10, 9, 8]]

Approach 1: Two Stacks

result = []
s1 [1]
s2 []

result = [1]
curr = 1
s1 []
s2 [2, 3]

result = [1, 3]
curr = 3
s1 [7, 6]
s2 [2]

result = [1, 3, 2]
curr = 2
s1 [7, 6, 5, 4]
s2 []

result = [1, 3, 2, 4, 5, 6, 7]
curr = 7
s1 []
s2 [8, 9, 10]

result = [1, 3, 2, 4, 5]
curr = 5
s1 [7, 6]
s2 [8, 9]

...

result = [1, 3, 2, 4, 5, 6, 7]
curr = 7
s1 []
s2 [8, 9, 10]

...

result = [1, 3, 2, 4, 5, 6, 7, 10, 9, 8]
curr = 7
s1 []
s2 []

                         q1         q2
Approach 2: 1 Dequeue [.......None......]

result = []
deque = [1, None]

result = [1, ]
curr = 1
deque = [None, 2, 3]

result = [1, 3]
curr = 3
deque = [6, 7, None, 2]

result = [1, 3, 2]
curr = 2
deque = [4, 5, 6, 7, None]

result = [1, 3, 2, 4]
curr = 4
deque = [5, 6, 7, None]
...
result = [1, 3, 2, 4, 5, 6, 7]
curr = 7
deque = [None, 8, 9, 10]

result = [1, 3, 2, 4, 5, 6, 7, 10]
curr = 10
deque = [None, 8, 9]
...
result = [1, 3, 2, 4, 5, 6, 7, 10, 9, 8]
curr = 8
deque = [None]

"""

def level_order_two_stacks(root):
    if not root: return None

    result = []
    stack1, stack2 = [root], []

    while stack1 or stack2:
        while stack1:
            node = stack1.pop()
            result.append(node.val)
            if node.left: stack2.append(node.left)
            if node.right: stack2.append(node.right)

        while stack2:
            node = stack2.pop()
            result.append(node.val)
            if node.right: stack1.append(node.right)
            if node.left: stack1.append(node.left)
            
    return result

#--------------------------------------------------

from collections import deque
def level_order_dequeue(root):
    if not root: return None
    
    result = []
    deq = deque([None])
    deq.appendleft(root)

    while len(deq) > 1:
        while deq[0] != None:
            node = deq.popleft()
            result.append(node.val)
            if node.left: deq.append(node.left)
            if node.right: deq.append(node.right)
        
        while deq[-1] != None:
            node = deq.pop()
            result.append(node.val)
            if node.right: deq.appendleft(node.right)
            if node.left: deq.appendleft(node.left)
    return result

#--------------------------------------------------

import unittest
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TestZigzagLevelOrder(unittest.TestCase):
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    root.left.left.left = BinaryTreeNode(8)
    root.left.right.left = BinaryTreeNode(9)
    root.right.right.right = BinaryTreeNode(10)

    def test_root_none(self):
        self.assertEqual(level_order_two_stacks(None), None)
        self.assertEqual(level_order_dequeue(None), None)

    def test_zigzag_level_order(self):
        self.assertEqual(level_order_two_stacks(self.root), [1, 3, 2, 4, 5, 6, 7, 10, 9, 8])
        self.assertEqual(level_order_dequeue(self.root), [1, 3, 2, 4, 5, 6, 7, 10, 9, 8])

if __name__ == "__main__": unittest.main()