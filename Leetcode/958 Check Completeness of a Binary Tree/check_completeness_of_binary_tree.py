import unittest
from collections import deque


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n), where n => number of nodes
# Space: O(n)
def check_completeness_of_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    first_none_found = False

    while queue:
        node = queue.pop()
        if not node:
            first_none_found = True

        else:
            if first_none_found:
                return False
            queue.appendleft(node.left)
            queue.appendleft(node.right)

    return True


class TestCompletenessOfBinaryTree(unittest.TestCase):
    def test_completeness(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)
        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.left = BTNode(6)

        self.assertTrue(check_completeness_of_binary_tree(root))

        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)
        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.right = BTNode(7)

        self.assertFalse(check_completeness_of_binary_tree(root))


if __name__ == "__main__":
    unittest.main()
