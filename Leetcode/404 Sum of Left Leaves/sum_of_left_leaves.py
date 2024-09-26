import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n), where n => number of nodes in BT
# Space: O(h), where h => height of BT ~ n
def recursive_helper(node, is_left_child, res):
    if not node.left and not node.right and is_left_child:
        res[0] += node.value
        return

    if node.left:
        recursive_helper(node.left, True, res)

    if node.right:
        recursive_helper(node.right, False, res)


def sum_of_left_leaves(root):
    res = [0]
    recursive_helper(root, False, res)
    return res[0]


class TestSumOfLeftLeaves(unittest.TestCase):
    def test_sum_of_left_leaves(self):
        root = BTNode(5)

        root.left = BTNode(3)
        root.right = BTNode(6)

        root.left.left = BTNode(2)
        root.left.right = BTNode(4)

        root.right.left = BTNode(10)
        root.right.right = BTNode(13)

        self.assertEqual(sum_of_left_leaves(root), 12)


if __name__ == "__main__":
    unittest.main()
