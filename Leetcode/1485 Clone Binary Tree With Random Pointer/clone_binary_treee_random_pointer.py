import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.random = None

    def __hash__(self):
        return id(self)


def recursive_helper_create_tree(node, clone_map):
    if not node:
        return None

    copy_node = BTNode(node.value)
    clone_map[node] = copy_node

    copy_node.left = recursive_helper_create_tree(node.left, clone_map)
    copy_node.right = recursive_helper_create_tree(node.right, clone_map)

    return copy_node


def recursive_helper_assign_random(node, clone_map):
    if not node:
        return

    clone_map[node].random = clone_map[node.random] if node.random else None
    recursive_helper_assign_random(node.left, clone_map)
    recursive_helper_assign_random(node.right, clone_map)


# Time: O(n), where n => number of nodes in tree
# Space: O(n)
def clone_binary_tree_random_pointer(root):
    clone_map = {}
    copy_root = recursive_helper_create_tree(root, clone_map)
    recursive_helper_assign_random(root, clone_map)
    return copy_root


class TestCloneBinaryTreeRandomPointer(unittest.TestCase):
    def assertTreesEqual(self, original, clone):
        """
        Helper function to verify that:
         - The structure and node values are the same.
         - The random pointers in the clone correspond to the same values as in the original.
         - The cloned nodes are distinct objects.
        """
        if original is None and clone is None:
            return
        # Ensure the cloned node is not the same instance as the original.
        self.assertIsNot(
            original, clone, "Cloned node should not be the same instance as original"
        )
        self.assertEqual(original.value, clone.value, "Node values should be equal")

        # Verify random pointers
        if original.random:
            self.assertIsNotNone(
                clone.random,
                "Cloned random pointer should not be None when original is not",
            )
            self.assertEqual(
                original.random.value,
                clone.random.value,
                "Random pointer values should match",
            )
        else:
            self.assertIsNone(
                clone.random,
                "Cloned node random should be None when original random is None",
            )

        self.assertTreesEqual(original.left, clone.left)
        self.assertTreesEqual(original.right, clone.right)

    def test_clone_binary_tree_random_pointer(self):
        # Build a sample tree:
        #         1
        #        / \
        #       2   3
        #      / \
        #     4   5
        node1 = BTNode(1)
        node2 = BTNode(2)
        node3 = BTNode(3)
        node4 = BTNode(4)
        node5 = BTNode(5)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5

        # Setting up random pointers:
        # 1.random -> 3, 2.random -> 1, 3.random -> 5, 4.random -> 3, 5.random -> 2
        node1.random = node3
        node2.random = node1
        node3.random = node5
        node4.random = node3
        node5.random = node2

        cloned_root = clone_binary_tree_random_pointer(node1)
        self.assertTreesEqual(node1, cloned_root)

    def test_clone_empty_tree(self):
        cloned = clone_binary_tree_random_pointer(None)
        self.assertIsNone(cloned, "Cloned tree of None should be None")


if __name__ == "__main__":
    unittest.main()
