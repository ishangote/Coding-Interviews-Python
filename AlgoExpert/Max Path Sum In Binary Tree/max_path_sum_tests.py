import unittest
from max_path_sum import maxPathSum, BTNode

class TestMaxPathSum(unittest.TestCase):
    def setUp(self) -> None:
        self.root = BTNode(1)
        self.root.left = BTNode(2)
        self.root.right = BTNode(3)
        self.root.left.left = BTNode(4)
        self.root.left.right = BTNode(5)
        self.root.right.left = BTNode(6)
        self.root.right.right = BTNode(7)
        return super().setUp()
    
    def test_generic(self):
        self.assertEqual(18, maxPathSum(self.root))

if __name__ == "__main__": unittest.main()