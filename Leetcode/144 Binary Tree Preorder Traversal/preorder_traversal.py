import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, res):
    res.append(node.value)

    if node.left:
        recursive_helper(node.left, res)

    if node.right:
        recursive_helper(node.right, res)

    return res


# Time: O(n), where n => number of nodes in BT
# Space: O(h), where h => height of BT (Implied space: recursive call stack)
def preorder_traversal_recursive(root):
    if not root:
        return []

    return recursive_helper(root, [])


# Time: O(n), where n => number of nodes in BT
# Space: O(h), where h => height of BT (Explicit space: defined stack) (in worst case h = n)
def preorder_traversal_iterative(root):
    if not root:
        return []

    res, stack = [], [root]

    while stack:
        node = stack.pop()
        res.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


class TestBinaryTreePreorderTraversal(unittest.TestCase):
    def test_preorder_traversal_recursive(self):
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
            preorder_traversal_recursive(root), [1, 2, 4, 5, 6, 7, 3, 8, 9]
        )

    def test_preorder_traversal_iterative(self):
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
            preorder_traversal_iterative(root), [1, 2, 4, 5, 6, 7, 3, 8, 9]
        )


if __name__ == "__main__":
    unittest.main()
