import unittest
from branch_sums_recursive import branchSumsRecursive, BinaryTree

class TestBrancSums(unittest.TestCase):
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(4)
    root.right.right = BinaryTree(5)

    """
        1
    2       3
           4  5
    """

    def test_branch_sums_generic(self):
        self.assertEqual(branchSumsRecursive(self.root), [3, 8, 9])

if __name__ == "__main__": unittest.main()