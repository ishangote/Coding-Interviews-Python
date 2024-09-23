import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node, current, res):
    current.append(node.value)

    if not node.left and not node.right:
        res.append("->".join(map(str, current)))

    else:
        if node.left:
            recursive_helper(node.left, current, res)

        if node.right:
            recursive_helper(node.right, current, res)

    current.pop()
    return


# Time: O(n * log(n)), where n => number of nodes in BT
# At each node, we are copying the current path to store it.
# The length of the path is proportional to the height of the tree, which is logN.
# Since this copying operation occurs for each node, and there are N nodes, this contributes an additional O(NlogN) complexity due to copying paths.
# Space: O(h), where h => height of BT (in worst case h = n)
def binary_tree_paths(root):
    if not root:
        return []

    res = []
    recursive_helper(root, [], res)

    return res


class TestBinaryTreePaths(unittest.TestCase):
    def test_binary_tree_paths_edge(self):
        self.assertEqual(binary_tree_paths(None), [])

        root = BTNode(1)
        self.assertEqual(binary_tree_paths(root), ["1"])

    def test_binary_tree_paths(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.right = BTNode(5)

        self.assertEqual(binary_tree_paths(root), ["1->2->5", "1->3"])


if __name__ == "__main__":
    unittest.main()
