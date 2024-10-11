import unittest


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def inorder_helper(node, inorder):
    if not node:
        return

    inorder_helper(node.left, inorder)
    inorder.append(node.value)
    inorder_helper(node.right, inorder)


# Time: O(n + n) ~ O(n) where n => number of nodes in BT
# Space: O(n)
def two_sum_iv(root, target):
    inorder = []

    inorder_helper(root, inorder)

    lo, hi = 0, len(inorder) - 1

    while lo < hi:
        if inorder[lo] + inorder[hi] == target:
            return True

        if inorder[lo] + inorder[hi] < target:
            lo += 1

        else:
            hi -= 1

    return False


class TestTwoSumIV(unittest.TestCase):
    def test_two_sum_iv_edge(self):
        self.assertFalse(two_sum_iv(BTNode(1), 2))

    def test_two_sum_iv(self):
        root = BTNode(5)

        root.left = BTNode(3)
        root.right = BTNode(6)

        root.left.left = BTNode(2)
        root.left.right = BTNode(4)
        root.right.right = BTNode(7)

        self.assertTrue(two_sum_iv(root, 12))
        self.assertTrue(two_sum_iv(root, 5))
        self.assertTrue(two_sum_iv(root, 9))
        self.assertTrue(two_sum_iv(root, 9))

        self.assertFalse(two_sum_iv(root, 28))
        self.assertFalse(two_sum_iv(root, -9))


if __name__ == "__main__":
    unittest.main()
