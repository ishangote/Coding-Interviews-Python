import unittest
from reconstruct_bst import BSTNode, reconstruct_tree_naive
class TestReconstructTree(unittest.TestCase):
    def setUp(self):
        left_subtree = BSTNode(4, BSTNode(2, BSTNode(1, None, None), None), BSTNode(5, None, None))
        right_subtree = BSTNode(17, None, BSTNode(19, BSTNode(18, None, None), None))
        self.root = BSTNode(10, left_subtree, right_subtree)

    def compare_trees(self, root1, root2):
        if not root1 and not root2: return True
        if (root1 and not root2) or (not root1 and root2) or root1.value != root2.value: return False
        return self.compare_trees(root1.left, root2.left) and self.compare_trees(root1.right, root2.right)
    
    def test_generic(self):
        self.assertEqual(True, self.compare_trees(self.root, reconstruct_tree_naive([10, 4, 2, 1, 5, 17, 19, 18])))

if __name__ == "__main__": unittest.main()