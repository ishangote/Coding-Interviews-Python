import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.left_element_helper(root)

    def left_element_helper(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # Time: O(1)
    def has_next(self):
        return not not self.stack

    # Time: O(n), where n => number of nodes in BST
    # Space: O(h), where h => height of BST ~ n
    def next(self):
        node = self.stack.pop()

        if node.right:
            self.left_element_helper(node.right)

        return node.value


class TestBSTIterator(unittest.TestCase):
    def test_bst_iterator(self):
        root = BTNode(7)

        root.left = BTNode(3)
        root.right = BTNode(15)

        root.right.left = BTNode(9)
        root.right.right = BTNode(20)

        bst_iterator = BSTIterator(root)

        self.assertEqual(bst_iterator.next(), 3)
        self.assertEqual(bst_iterator.next(), 7)
        self.assertTrue(bst_iterator.has_next())
        self.assertEqual(bst_iterator.next(), 9)
        self.assertTrue(bst_iterator.has_next())
        self.assertEqual(bst_iterator.next(), 15)
        self.assertTrue(bst_iterator.has_next())
        self.assertEqual(bst_iterator.next(), 20)
        self.assertFalse(bst_iterator.has_next())


if __name__ == "__main__":
    unittest.main()
