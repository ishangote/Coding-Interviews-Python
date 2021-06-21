import unittest
from reverse_inorder import kth_largest_value_reverse_inorder
from inorder import kth_largest_value_inorder
from inorder import BSTNode

class TestKthLargestValueInBST(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(15)
        self.root.right = BSTNode(20)
        self.root.right.right = BSTNode(22)
        self.root.right.left = BSTNode(17)
        self.root.left = BSTNode(5)
        self.root.left.right = BSTNode(5)
        self.root.left.left = BSTNode(2)
        self.root.left.left.right = BSTNode(3)
        self.root.left.left.left = BSTNode(1)

    def test_inorder(self):
        self.assertEqual(17, kth_largest_value_inorder(self.root, 3))
    
    def test_reverse_inorder(self):
        self.assertEqual(17, kth_largest_value_reverse_inorder(self.root, 3))

if __name__ == "__main__": unittest.main()