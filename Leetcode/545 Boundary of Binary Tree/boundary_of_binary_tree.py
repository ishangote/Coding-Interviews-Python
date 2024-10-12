import unittest


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def evaluate_left_boundary(node, res):
    if not node or (not node.left and not node.right):
        return

    res.append(node.value)

    if node.left:
        evaluate_left_boundary(node.left, res)

    elif node.right:
        evaluate_left_boundary(node.right, res)


def evaluate_bottom_boundary(node, res):
    if not node:
        return

    if not node.left and not node.right:
        res.append(node.value)

    evaluate_bottom_boundary(node.left, res)
    evaluate_bottom_boundary(node.right, res)


def evaluate_right_boundary(node, res):
    if not node or (not node.left and not node.right):
        return

    if node.right:
        evaluate_right_boundary(node.right, res)

    elif node.left:
        evaluate_right_boundary(node.left, res)

    res.append(node.value)


# Time: O(n), where n => number of nodes in BT
# Space: O(n), implied call stack memory
def boundary_of_binary_tree(root):
    if not root.left and not root.right:
        return [root.value]

    res = [root.value]

    evaluate_left_boundary(root.left, res)
    evaluate_bottom_boundary(root, res)
    evaluate_right_boundary(root.right, res)

    return res


class TestBoundaryOfBinaryTree(unittest.TestCase):
    def test_boundary_of_binary_tree_edge(self):
        self.assertEqual(boundary_of_binary_tree(BTNode(4)), [4])

    def test1_boundary_of_binary_tree(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(6)
        root.right.left = BTNode(5)
        root.right.right = BTNode(7)

        root.left.right.left = BTNode(8)
        root.right.right.left = BTNode(9)

        self.assertEqual(boundary_of_binary_tree(root), [1, 2, 4, 8, 5, 9, 7, 3])

    def test2_boundary_of_binary_tree(self):
        root = BTNode(1)

        root.left = BTNode(2)
        root.right = BTNode(3)

        root.left.left = BTNode(4)
        root.left.right = BTNode(5)
        root.right.left = BTNode(6)

        root.left.right.left = BTNode(7)
        root.left.right.right = BTNode(8)
        root.right.left.left = BTNode(9)
        root.right.left.right = BTNode(10)

        self.assertEqual(boundary_of_binary_tree(root), [1, 2, 4, 7, 8, 9, 10, 6, 3])


if __name__ == "__main__":
    unittest.main()
