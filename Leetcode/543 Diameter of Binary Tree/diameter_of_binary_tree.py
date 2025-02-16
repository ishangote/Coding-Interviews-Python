import unittest


class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recursive_helper(root, res):
    if not root:
        return 0

    left_height = recursive_helper(root.left, res)
    right_height = recursive_helper(root.right, res)

    res[0] = max(res[0], 1 + left_height + right_height)
    return 1 + max(left_height, right_height)


# Time: O(n), where n => number of nodes in BT
# Space: O(n)
def diameter_of_binary_tree(root):
    if not root:
        return 0
    res = [0]
    recursive_helper(root, res)
    return res[0] - 1


class TestDiameterOfBinaryTree(unittest.TestCase):
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.right.left = BTNode(5)
    root.right.left.right = BTNode(6)

    def test_diameter_of_binary_tree(self):
        self.assertEqual(diameter_of_binary_tree(self.root), 5)


if __name__ == "__main__":
    unittest.main()
