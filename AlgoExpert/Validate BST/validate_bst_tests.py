import unittest
from validate_bst import validate_bst
from validate_bst import BSTNode

class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(10)
        self.root.left = BSTNode(5)
        self.root.right = BSTNode(15)
        self.root.left.left = BSTNode(2)
        self.root.left.left.left = BSTNode(1)
        self.root.left.right = BSTNode(5)

        self.root1 = BSTNode(10)
        self.root1.left = BSTNode(5)
        self.root1.right = BSTNode(15)
        self.root1.left.left = BSTNode(2)
        self.root1.left.left.left = BSTNode(2)
        self.root1.left.right = BSTNode(5)

    def test_generic(self):
        self.assertEqual(True, validate_bst(self.root))
        self.assertEqual(False, validate_bst(self.root1))

if __name__ == "__main__": unittest.main()