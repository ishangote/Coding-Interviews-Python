class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from collections import deque
# Time: O(n), n => number of nodes in BT
# Space: O(n), n => number of nodes in BT
def binary_tree_right_side_view(root):
    if not root: return []
    level_order_nodes = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.pop()
        
        if level >= len(level_order_nodes): level_order_nodes.append([])
        level_order_nodes[level].append(node.value)

        if node.left: queue.appendleft((node.left, level + 1))
        if node.right: queue.appendleft((node.right, level + 1))
    
    res = []
    for level in level_order_nodes:
        res.append(level[-1])
    
    return res

import unittest
class TestBinaryTreeRightSideView(unittest.TestCase):
    def test_binary_tree_right_side_view_base_case(self):
        self.assertEqual(binary_tree_right_side_view(None), [])

    def test_binary_tree_right_side_view(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.left = BTNode(6)
        root.right.right = BTNode(7)

        root.left.right.left = BTNode(8)

        self.assertEqual(binary_tree_right_side_view(root), [1, 3, 7, 8])

if __name__ == "__main__": unittest.main()
