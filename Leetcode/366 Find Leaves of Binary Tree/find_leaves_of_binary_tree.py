import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, leaf_nodes):
    if not node:
        return None

    if not node.left and not node.right:
        leaf_nodes.append(node.value)
        return None

    node.left = recursive_helper(node.left, leaf_nodes)
    node.right = recursive_helper(node.right, leaf_nodes)
    return node


# Time: O(n), where n => number of nodes in BT
# Space: O(n)
def find_leaves_simulation(root):
    res = []

    while root:
        leaf_nodes = []
        root = recursive_helper(root, leaf_nodes)
        res.append(leaf_nodes)

    return res


class TestFindLeavesOfBinaryTree(unittest.TestCase):
    def test_find_leaves_simulation(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)
        root.left.left = BTNode(4)
        root.left.right = BTNode(5)

        self.assertListEqual(find_leaves_simulation(root), [[4, 5, 3], [2], [1]])


if __name__ == "__main__":
    unittest.main()
