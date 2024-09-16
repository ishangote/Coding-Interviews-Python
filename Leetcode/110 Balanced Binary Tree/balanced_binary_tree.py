import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def calculate_max_height(node):
    if not node:
        return 0

    return 1 + max(calculate_max_height(node.left), calculate_max_height(node.right))


# Time: O(n^2) where n => number of nodes
# Space: O(n^2)
def balanced_binary_tree_brute_force(root):
    if not root:
        return True

    max_left_height = calculate_max_height(root.left)
    max_right_height = calculate_max_height(root.right)

    return (
        abs(max_left_height - max_right_height) <= 1
        and balanced_binary_tree_brute_force(root.left)
        and balanced_binary_tree_brute_force(root.right)
    )


def recursive_helper(node):
    if not node:
        return (True, 0)

    is_balanced_bt_left, max_left_height = recursive_helper(node.left)
    is_balanced_bt_right, max_right_height = recursive_helper(node.right)

    is_balanced_bt = (
        is_balanced_bt_left
        and is_balanced_bt_right
        and abs(max_left_height - max_right_height) <= 1
    )

    return (is_balanced_bt, 1 + max(max_left_height, max_right_height))


# Time: O(n), where n => number of nodes
# Space: O(h), where h => height of BT
def balanced_binary_tree_optimized(root):
    return recursive_helper(root)[0]


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_binary_tree_brute_force(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(2)

        root.left.left = BTNode(3)
        root.right.right = BTNode(3)

        root.left.left.left = BTNode(4)
        root.right.right.right = BTNode(4)

        self.assertEqual(balanced_binary_tree_brute_force(root), False)

    def test_balanced_binary_tree_optimized(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(2)

        root.left.left = BTNode(3)
        root.right.right = BTNode(3)

        root.left.left.left = BTNode(4)
        root.right.right.right = BTNode(4)

        self.assertEqual(balanced_binary_tree_optimized(root), False)


if __name__ == "__main__":
    unittest.main()
