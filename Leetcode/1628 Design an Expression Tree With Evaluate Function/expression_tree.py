import unittest


class ETNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def recursive_helper(self, node):
        if not node.left and not node.right:
            return int(node.value)

        left_evaluation = self.recursive_helper(node.left)
        right_evaluation = self.recursive_helper(node.right)

        if node.value == "/":
            return left_evaluation // right_evaluation

        elif node.value == "*":
            return left_evaluation * right_evaluation

        elif node.value == "+":
            return left_evaluation + right_evaluation

        else:
            return left_evaluation - right_evaluation

    # Time: O(n), where n => number of nodes in ET
    # Space: O(n)
    def evaluate(self):
        return self.recursive_helper(self)


class TreeBuilder:
    # Time: O(n), where n => length of postfix
    # Space: O(n)
    def build_tree(self, postfix):
        stack = []

        for op in postfix:
            op_node = ETNode(op)

            if not op.isdigit():
                op_node.right = stack.pop()
                op_node.left = stack.pop()

            stack.append(op_node)

        return stack.pop()


class TestExpressionTree(unittest.TestCase):
    def test1_build_tree(self):
        root = TreeBuilder().build_tree(["3", "4", "+", "2", "*", "7", "/"])

        self.assertEqual(root.left.value, "*")
        self.assertEqual(root.right.value, "7")

        self.assertEqual(root.left.left.value, "+")
        self.assertEqual(root.left.right.value, "2")

        self.assertEqual(root.left.left.left.value, "3")
        self.assertEqual(root.left.left.right.value, "4")

        self.assertEqual(root.evaluate(), 2)

    def test2_build_tree(self):
        root = TreeBuilder().build_tree(["4", "5", "2", "7", "+", "-", "*"])

        self.assertEqual(root.value, "*")

        self.assertEqual(root.left.value, "4")
        self.assertEqual(root.right.value, "-")

        self.assertEqual(root.right.left.value, "5")
        self.assertEqual(root.right.right.value, "+")

        self.assertEqual(root.right.right.left.value, "2")
        self.assertEqual(root.right.right.right.value, "7")

        self.assertEqual(root.evaluate(), -16)


if __name__ == "__main__":
    unittest.main()
