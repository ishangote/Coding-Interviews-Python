class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten_helper(node):
    # Base Case
    if not node: return None
    if not node.left and not node.right: return node

    left_tail = flatten_helper(node.left)
    right_tail = flatten_helper(node.right)

    if node.left:
        left_tail.right = node.right
        node.right = node.left
        node.left = None
    
    return right_tail or left_tail or node

# Time: O(n), n => number of nodes in BT
# Space: (h), h => height of BT i.e in worst case h = n (Implied call stack memory)
def flatten_binary_tree(root: BTNode):
    flatten_helper(root)

import unittest
class TestFlattenBinaryTreeToLinkedList(unittest.TestCase):
    def test_flatten_binary_tree_base_case(self):
        root = None
        flatten_binary_tree(root)
        self.assertEqual(root, None)

    def test_flatten_binary_tree(self):
        root = BTNode(1)
        
        root.left = BTNode(2)
        root.right = BTNode(5)

        root.left.left = BTNode(3)
        root.left.right = BTNode(4)

        root.right.right = BTNode(6)

        flatten_binary_tree(root)

        self.assertEqual(root.value, 1)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right.value, 2)
        self.assertEqual(root.right.right.value, 3)
        self.assertEqual(root.right.right.right.value, 4)
        self.assertEqual(root.right.right.right.right.value, 5)
        self.assertEqual(root.right.right.right.right.right.value, 6)

if __name__ == "__main__": unittest.main()
