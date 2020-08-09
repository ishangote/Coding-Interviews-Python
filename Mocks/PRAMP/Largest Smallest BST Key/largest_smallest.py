"""
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

For example:

For num = 17 and the binary search tree below:

                  20
            9           25
        5      12
             11  14

Your function would return:
14 since it’s the largest key in the tree that is still smaller than 17.


n = 4


"""

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#iterative
def largest_smallest(root, target):
    ans = -1
    while root:
        if root.val < target:
            ans = root.val
            root = root.right
        else:
            root = root.left
    return ans

import unittest
class TestLargestSmallestBSTKey(unittest.TestCase):
    root = BSTNode(20)
    root.left = BSTNode(9)
    root.right = BSTNode(25)
    root.left.left = BSTNode(5)
    root.left.right = BSTNode(12)
    root.left.right.left = BSTNode(11)
    root.left.right.right = BSTNode(14)

    def test_pramp_example(self):
        self.assertEqual(largest_smallest(self.root, 17), 14)
        self.assertEqual(largest_smallest(self.root, 4), -1)
        self.assertEqual(largest_smallest(self.root, 8), 5)

if __name__ == "__main__": unittest.main()