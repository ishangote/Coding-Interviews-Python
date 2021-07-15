import unittest
from find_nodes_distance_k import BTNode, findNodesDistanceK

class TestFindNodesDistanceK(unittest.TestCase):
    def setUp(self) -> None:
        self.root = BTNode(1)
        self.root.left = BTNode(2)
        self.root.right = BTNode(3)
        self.root.left.left = BTNode(4)
        self.root.left.right = BTNode(5)
        self.root.right.right = BTNode(6)
        self.root.right.right.left = BTNode(7)
        self.root.right.right.right = BTNode(8)

        return super().setUp()

    def test_generic(self):
        self.assertCountEqual([7, 8, 2], findNodesDistanceK(self.root, 3, 2))
        self.assertCountEqual([1, 6], findNodesDistanceK(self.root, 3, 1))
        self.assertCountEqual([4, 5], findNodesDistanceK(self.root, 3, 3))

if __name__ == "__main__": unittest.main()