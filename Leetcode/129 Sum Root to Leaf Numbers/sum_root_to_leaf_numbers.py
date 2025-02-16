import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, cur, res):
    cur = cur * 10 + node.value

    if not node.left and not node.right:
        res.append(cur)
        return

    if node.left:
        recursive_helper(node.left, cur, res)

    if node.right:
        recursive_helper(node.right, cur, res)


# Time: O(n), where n => number of nodes in BT
# Space: O(n), implied call stack memory
def sum_root_to_leaf_numbers_recursive(root):
    if not root:
        return 0

    res = []
    recursive_helper(root, 0, res)
    return sum(res)


# -------------------------------------------------- #


def sum_root_to_leaf_numbers_iterative(root):
    if not root:
        return 0
    stack = [(root, root.value)]
    result = 0
    while stack:
        node, node_val = stack.pop()
        # Condition to check if current node is leaf node:
        if not node.left and not node.right:
            result += node_val
        if node.right:
            stack.append((node.right, node_val * 10 + node.right.value))
        if node.left:
            stack.append((node.left, node_val * 10 + node.left.value))
    return result


class TestSumRootToLeafNumbers(unittest.TestCase):
    def test_sum_root_to_leaf_numbers_recursive(self):
        self.assertEqual(sum_root_to_leaf_numbers_recursive(None), 0)
        self.assertEqual(sum_root_to_leaf_numbers_recursive(BTNode(1)), 1)

        root = BTNode(4)
        root.left = BTNode(9)
        root.left.left = BTNode(5)
        root.left.right = BTNode(1)
        root.right = BTNode(0)

        self.assertEqual(sum_root_to_leaf_numbers_recursive(root), 1026)

        root1 = BTNode(1)
        root1.left = BTNode(2)
        root1.right = BTNode(3)

        self.assertEqual(sum_root_to_leaf_numbers_recursive(root1), 25)

    def test_sum_root_to_leaf_numbers_iterative(self):
        self.assertEqual(sum_root_to_leaf_numbers_iterative(None), 0)
        self.assertEqual(sum_root_to_leaf_numbers_iterative(BTNode(1)), 1)

        root = BTNode(4)
        root.left = BTNode(9)
        root.left.left = BTNode(5)
        root.left.right = BTNode(1)
        root.right = BTNode(0)

        self.assertEqual(sum_root_to_leaf_numbers_iterative(root), 1026)

        root1 = BTNode(1)
        root1.left = BTNode(2)
        root1.right = BTNode(3)

        self.assertEqual(sum_root_to_leaf_numbers_iterative(root1), 25)


if __name__ == "__main__":
    unittest.main()
