import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recursive_helper(node):
    if not node:
        return "()"

    left_expression = recursive_helper(node.left)
    right_expression = recursive_helper(node.right)

    if left_expression == "()" and right_expression == "()":
        return f"({node.value})"

    return f"({node.value}{left_expression}{right_expression if right_expression != '()' else ''})"


# Time: O(n), where n => number of nodes in BT
# Space: O(n)
def construct_string_from_binary_tree(root):
    res = recursive_helper(root)
    return res[1:-1]


class TestConstructStringFromBinaryTree(unittest.TestCase):
    def test1_construct_string_from_binary_tree(self):
        # Original test case:
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)
        root.left.left = BTNode(4)
        self.assertEqual(construct_string_from_binary_tree(root), "1(2(4))(3)")

    def test2_construct_string_from_binary_tree(self):
        root = BTNode(1)
        root.left = BTNode(2)
        root.right = BTNode(3)
        root.left.right = BTNode(4)
        self.assertEqual(construct_string_from_binary_tree(root), "1(2()(4))(3)")


if __name__ == "__main__":
    unittest.main()
