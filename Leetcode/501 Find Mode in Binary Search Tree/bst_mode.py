import unittest
from collections import defaultdict
import sys


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Brute Force
# -------------------------------------------------------- #


def recursive_helper(node, count_map):
    count_map[node.value] += 1

    if node.left:
        recursive_helper(node.left, count_map)

    if node.right:
        recursive_helper(node.right, count_map)


# Time: O(n), where n => number of nodes in bst
# Space: O(n)
def bst_mode_brute_force(root):
    count_map = defaultdict(lambda: 1)

    recursive_helper(root, count_map)

    return [
        node_val
        for node_val, count in count_map.items()
        if count == max(count_map.values())
    ]


# In-order Traversal
# -------------------------------------------------------- #


def inorder_helper(node, cur, cur_freq, max_freq, res):
    if not node:
        return

    inorder_helper(node.left, cur, cur_freq, max_freq, res)

    if cur[0] != node.value:
        cur[0] = node.value
        cur_freq[0] = 0

    cur_freq[0] += 1

    if cur_freq[0] > max_freq[0]:
        # Update the original list using slice assignment
        # res = [cur[0]] will not work since this does not modify the original list `res` passed to the function.
        # Instead, it reassigns res to a new list
        res[:] = [cur[0]]
        max_freq[0] = cur_freq[0]

    elif cur_freq[0] == max_freq[0]:
        res.append(cur[0])

    else:
        pass

    inorder_helper(node.right, cur, cur_freq, max_freq, res)


# Time: O(n), where n => number of nodes in BT
# Space: O(1), excluding the implied call stack memory for recursion
def bst_mode_inorder(root):
    res = []
    cur, cur_freq, max_freq = [-sys.maxsize], [0], [0]

    inorder_helper(root, cur, cur_freq, max_freq, res)

    return res


# -------------------------------------------------------- #


class BinarySearchTreeMode(unittest.TestCase):
    def test_bst_mode_brute_force(self):
        root = BTNode(3)

        root.left = BTNode(1)
        root.right = BTNode(3)

        root.left.left = BTNode(1)
        root.left.right = BTNode(2)

        root.left.right.right = BTNode(3)

        self.assertListEqual(bst_mode_brute_force(root), [3])

    def test_bst_mode_inorder(self):
        root = BTNode(3)

        root.left = BTNode(1)
        root.right = BTNode(3)

        root.left.left = BTNode(1)
        root.left.right = BTNode(2)

        root.left.left.left = BTNode(1)
        root.left.right.right = BTNode(3)

        self.assertListEqual(bst_mode_inorder(root), [1, 3])


if __name__ == "__main__":
    unittest.main()
