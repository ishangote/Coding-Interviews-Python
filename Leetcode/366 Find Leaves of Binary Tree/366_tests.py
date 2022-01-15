import unittest
from utils.BTNode import BTNode
from find_leaves_of_binary_tree import find_leaves

class TestFindLeavesOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt0 = None
        self.bt0_expected = []

        self.bt1 = BTNode('a')
        self.bt1_expected = [['a']]

        self.bt2 = BTNode(1)
        self.bt2.left = BTNode(2)
        self.bt2.right = BTNode(3)
        self.bt2.left.left = BTNode(4)
        self.bt2.left.right = BTNode(5)
        self.bt2_expected = [[4, 5, 3], [2], [1]]

    def test_find_leaves_of_binary_tree(self):
        self.assertListEqual(find_leaves(self.bt0), self.bt0_expected)
        self.assertListEqual(find_leaves(self.bt1), self.bt1_expected)
        self.assertListEqual(find_leaves(self.bt2), self.bt2_expected)

if __name__ == '__main__': unittest.main()