import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, res):
    if node.left:
        recursive_helper(node.left, res)

    if node.right:
        recursive_helper(node.right, res)

    res.append(node.value)

    return res


def postorder_traversal_recursive(root):
    if not root:
        return []

    return recursive_helper(root, [])


class TestBinaryTreePostorderTraversal(unittest.TestCase):
    def test_postorder_traversal_recursive(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.right = BTNode(8)

        root.left.right.left = BTNode(6)
        root.left.right.right = BTNode(7)
        root.right.right.left = BTNode(9)

        self.assertEqual(
            postorder_traversal_recursive(root), [4, 6, 7, 5, 2, 9, 8, 3, 1]
        )


if __name__ == "__main__":
    unittest.main()
