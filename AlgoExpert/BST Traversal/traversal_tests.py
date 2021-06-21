import unittest
from bst_traversal import BSTNode, inorder, preorder, postorder

class TestBSTTraversal(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(10)
        self.root.left = BSTNode(5)
        self.root.right = BSTNode(15)
        self.root.left.left = BSTNode(2)
        self.root.left.left.left = BSTNode(1)
        self.root.left.right = BSTNode(5)

    """
          10
        5    15
      2   5
    1
    """
    
    def test_inorder(self):
        self.assertEqual([1, 2, 5, 5, 10, 15], inorder(self.root, []))

    def test_preorder(self):
        self.assertEqual([10, 5, 2, 1, 5, 15], preorder(self.root, []))

    def test_postorder(self):
        self.assertEqual([1, 2, 5, 5, 15, 10], postorder(self.root, []))

if __name__ == "__main__": unittest.main()