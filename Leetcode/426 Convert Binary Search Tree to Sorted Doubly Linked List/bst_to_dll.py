import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node):
    if not node:
        return (None, None)

    left_head, left_tail = recursive_helper(node.left)
    node.left = left_tail
    if left_tail:
        left_tail.right = node

    right_head, right_tail = recursive_helper(node.right)
    node.right = right_head
    if right_head:
        right_head.left = node

    head = left_head if left_head else node
    tail = right_tail if right_tail else node

    return (head, tail)


# Time: O(n), where n => number of nodes in BT
# Space: O(h), where h => height of BT ~ n
def bst_to_dll(root):
    head, tail = recursive_helper(root)

    if head:
        head.left = tail

    if tail:
        tail.right = head

    return head


class TestBSTToDLL(unittest.TestCase):
    def test_bst_to_dll(self):
        root = BTNode(4)

        root.left = BTNode(2)
        root.right = BTNode(5)

        root.left.left = BTNode(1)
        root.left.right = BTNode(3)

        head = bst_to_dll(root)

        self.assertEqual(head.value, 1)
        self.assertEqual(head.left.value, 5)
        self.assertEqual(head.right.value, 2)
        self.assertEqual(head.right.left.value, 1)
        self.assertEqual(head.right.right.value, 3)
        self.assertEqual(head.right.right.left.value, 2)
        self.assertEqual(head.right.right.right.value, 4)
        self.assertEqual(head.right.right.right.left.value, 3)
        self.assertEqual(head.right.right.right.right.value, 5)
        self.assertEqual(head.right.right.right.right.right.value, 1)
        self.assertEqual(head.right.right.right.right.left.value, 4)


if __name__ == "__main__":
    unittest.main()
