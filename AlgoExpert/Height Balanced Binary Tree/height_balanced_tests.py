import unittest
from height_balanced import *
class TestHeightBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BTNode(1)
        self.root.left = BTNode(2)
        self.root.right = BTNode(3)
        self.root.left.left = BTNode(4)
        self.root.left.right = BTNode(5)
        self.root.right.right = BTNode(6)
        self.root.left.right.left = BTNode(7)
        self.root.left.right.right = BTNode(8)
    
    def test_generic(self):
        self.assertEqual(True, is_balanced(self.root))

if __name__ == "__main__": unittest.main()