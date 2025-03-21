import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, lo, hi, res):
    if not node:
        return

    if lo <= node.value <= hi:
        res[0] += node.value

    # Move to the left as we might have smaller values than current
    if lo < node.value:
        recursive_helper(node.left, lo, hi, res)
    # Move to the right as we might have larger values than current
    if node.value < hi:
        recursive_helper(node.right, lo, hi, res)


# Time: O(n), where n => number of nodes in BST
# Space: O(n)
def range_sum_of_bst(root, lo, hi):
    res = [0]
    recursive_helper(root, lo, hi, res)
    return res[0]


class TestRangeSumOfBst(unittest.TestCase):
    def test_range_sum_of_bst(self):
        root = BTNode(10)

        root.left = BTNode(5)
        root.right = BTNode(15)

        root.left.left = BTNode(3)
        root.left.right = BTNode(7)
        root.right.left = BTNode(13)
        root.right.right = BTNode(18)

        root.left.left.left = BTNode(1)
        root.left.right.left = BTNode(6)

        self.assertEqual(range_sum_of_bst(root, 6, 10), 23)


if __name__ == "__main__":
    unittest.main()
