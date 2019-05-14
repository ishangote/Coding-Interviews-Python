"""
    T1    +     T2      =      T3
    4           1               5
   /  \        / \           /    \
  7    2      5   2         12     4
   \             / \         \    / \
    2           4   3         2  4   3

[4,7,2,2]    [1,5,2,4,3]   [5,12,4,2,4,3]

"""
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def merge_trees(T1, T2):
    if T1 == None: return T2
    if T2 == None: return T1

    T1.val += T2.val

    T1.left = merge_trees(T1.left, T2.left)
    T1.right = merge_trees(T1.right, T2.right)

    return T1

#----------------------------------------------
#TESTING...

#Level-order traversal helper to print...
import queue
def level_order_print(root):
    print_result = []
    q = queue.Queue()
    if root != None: q.put(root)
    while not q.empty():
        temp = q.get()
        print_result.append(temp.val)
        if temp.left: q.put(temp.left)
        if temp.right: q.put(temp.right)
    return print_result

import unittest
class TestMergeBinaryTrees(unittest.TestCase):
    def test_t2_none(self):
        T1 = BinaryTreeNode(2)
        T1.left = BinaryTreeNode(3)
        T1.right = BinaryTreeNode(1)
        self.assertEqual(level_order_print(merge_trees(T1, None)), [2, 3, 1])

    def test_t1_none(self):
        T2 = BinaryTreeNode(2)
        T2.left = BinaryTreeNode(3)
        T2.right = BinaryTreeNode(1)
        self.assertEqual(level_order_print(merge_trees(None, T2)), [2, 3, 1])

    def test_both_none(self):
        self.assertEqual(level_order_print(merge_trees(None, None)), [])

    def test_merge_trees(self):
        T1 = BinaryTreeNode(2)
        T1.left = BinaryTreeNode(3)
        T1.right = BinaryTreeNode(1)
        T1.left.left = BinaryTreeNode(4)
        T1.right.right = BinaryTreeNode(7)

        T2 = BinaryTreeNode(3)
        T2.left = BinaryTreeNode(2)
        T2.right = BinaryTreeNode(4)
        T2.left.right = BinaryTreeNode(1)
        T2.right.right = BinaryTreeNode(5)

        self.assertEqual(level_order_print(merge_trees(T1, T2)), [5, 5, 5, 4, 1, 12])

if __name__ == "__main__": unittest.main()