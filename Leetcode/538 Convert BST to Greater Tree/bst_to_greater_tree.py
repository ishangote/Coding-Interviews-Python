import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, cur_sum):
    if not node:
        return

    recursive_helper(node.right, cur_sum)
    cur_sum[0] += node.value
    node.value = cur_sum[0]
    recursive_helper(node.left, cur_sum)


# Time: O(n), where n => number of nodes in BST
# Space: O(n), implied call stack memory
def bst_to_greater_tree(root):
    recursive_helper(root, [0])
    return root


class TestBSTToGreaterTree(unittest.TestCase):
    def test_bst_to_greater_tree(self):
        root = BTNode(10)

        root.left = BTNode(5)
        root.right = BTNode(20)

        root.left.left = BTNode(1)
        root.left.right = BTNode(6)
        root.right.left = BTNode(15)
        root.right.right = BTNode(30)

        bst_to_greater_tree(root)

        self.assertEqual(root.value, 75)

        self.assertEqual(root.left.value, 86)
        self.assertEqual(root.right.value, 50)

        self.assertEqual(root.left.left.value, 87)
        self.assertEqual(root.left.right.value, 81)
        self.assertEqual(root.right.left.value, 65)
        self.assertEqual(root.right.right.value, 30)


if __name__ == "__main__":
    unittest.main()
