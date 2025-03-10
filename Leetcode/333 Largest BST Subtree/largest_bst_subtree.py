import unittest
import sys


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, res):
    if not node:
        return (sys.maxsize, -sys.maxsize, True, 0)

    left_min, left_max, left_is_bst, left_bst_size = recursive_helper(node.left, res)
    right_min, right_max, right_is_bst, right_bst_size = recursive_helper(
        node.right, res
    )

    if left_is_bst and right_is_bst and left_max < node.value < right_min:
        current_size = left_bst_size + right_bst_size + 1
        res[0] = max(res[0], current_size)
        return (
            min(left_min, node.value),
            max(right_max, node.value),
            True,
            current_size,
        )

    # return dummy min and max values (sys.maxsize, -sys.maxsize) because they won't be used
    return (sys.maxsize, -sys.maxsize, False, max(left_bst_size, right_bst_size))


# Time: O(n), where n => number of nodes in tree
# Space: O(n)
def largest_bst_subtree(root):
    res = [0]
    recursive_helper(root, res)
    return res[0]


class TestLargestBSTSubtree(unittest.TestCase):
    def test_largest_bst_subtree(self):
        #      10
        #     /  \
        #    9   12
        #   / \
        #  1   8
        # The whole tree is not a BST because 9's right child 8 is less than 9.
        # Valid BST subtrees are the individual nodes, so largest BST size is 1.
        root = BTNode(10)
        root.left = BTNode(9)
        root.right = BTNode(12)
        root.left.left = BTNode(1)
        root.left.right = BTNode(8)
        self.assertEqual(largest_bst_subtree(root), 1)

    def test_entire_tree_bst(self):
        # Entire tree is a BST.
        #         10
        #        /   \
        #       5     15
        #      / \   /  \
        #     1   8 12  20
        # Largest BST is the entire tree with 7 nodes.
        root = BTNode(10)
        root.left = BTNode(5)
        root.right = BTNode(15)
        root.left.left = BTNode(1)
        root.left.right = BTNode(8)
        root.right.left = BTNode(12)
        root.right.right = BTNode(20)
        self.assertEqual(largest_bst_subtree(root), 7)

    def test_empty_tree(self):
        # Edge case: empty tree should return 0.
        self.assertEqual(largest_bst_subtree(None), 0)

    def test_single_node(self):
        # Edge case: tree with only one node is a BST of size 1.
        root = BTNode(42)
        self.assertEqual(largest_bst_subtree(root), 1)

    def test_bst_in_one_subtree(self):
        # Tree where BST property fails at the root.
        #      10
        #     /  \
        #   15   20   -> 15 > 10 violates BST for left subtree.
        # In this case, no multi-node BST exists; largest valid BST is any single node.
        root = BTNode(10)
        root.left = BTNode(15)  # Violation: left child is greater than root.
        root.right = BTNode(20)
        self.assertEqual(largest_bst_subtree(root), 1)

    def test_bst_in_one_child(self):
        # Tree where one child subtree is a valid BST.
        #          10
        #         /   \
        #        5     15
        #       / \    /  \
        #      1   8  7    20
        # Here, the overall tree is not a BST because 7 (in right subtree) is less than 10.
        # The left subtree (5-1-8) is a valid BST with 3 nodes.
        # The right subtree (15-7-20) is valid when considered on its own (3 nodes) but fails at 10.
        # Largest valid BST subtree size is 3.
        root = BTNode(10)
        root.left = BTNode(5)
        root.right = BTNode(15)
        root.left.left = BTNode(1)
        root.left.right = BTNode(8)
        root.right.left = BTNode(
            7
        )  # Although valid locally, causes parent's violation.
        root.right.right = BTNode(20)
        self.assertEqual(largest_bst_subtree(root), 3)


if __name__ == "__main__":
    unittest.main()
