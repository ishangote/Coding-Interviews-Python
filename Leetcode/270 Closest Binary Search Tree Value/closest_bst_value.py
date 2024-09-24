import unittest


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def recursive_helper(node, target, min_distance_node):
    distance = abs(node.value - target)

    if distance == min_distance_node[0]:
        if node.value < min_distance_node[1].value:
            min_distance_node = (distance, node)

    if distance < min_distance_node[0]:
        min_distance_node = (distance, node)

    if target <= node.value and node.left:
        min_distance_node = recursive_helper(node.left, target, min_distance_node)

    elif target > node.value and node.right:
        min_distance_node = recursive_helper(node.right, target, min_distance_node)

    return min_distance_node


# Time: O(logn), where n => number of nodes in BST
# Space: O(logn)
def closest_bst_value_recursive(root, target):
    min_distance_node = recursive_helper(root, target, [float("inf"), None])
    return min_distance_node[1].value


# Time: O(logn)
# Space: O(1)
def closest_bst_value_iterative(root, target):
    min_distance, min_distance_node = float("inf"), None
    runner = root

    while runner:
        distance = abs(runner.value - target)

        if distance == min_distance:
            min_distance_node = (
                runner if runner.value < min_distance_node.value else min_distance_node
            )

        if distance < min_distance:
            min_distance_node = runner
            min_distance = distance

        if target <= runner.value:
            runner = runner.left

        else:
            runner = runner.right

    return min_distance_node.value


class TestClosestBSTValue(unittest.TestCase):
    def test_closest_bst_value_recursive(self):
        self.root = BTNode(4)

        self.root.left = BTNode(2)
        self.root.right = BTNode(5)

        self.root.left.left = BTNode(1)
        self.root.left.right = BTNode(3)

        self.assertEqual(closest_bst_value_recursive(self.root, 3.714286), 4)

    def test_closest_bst_value_iterative(self):
        self.root = BTNode(4)

        self.root.left = BTNode(2)
        self.root.right = BTNode(5)

        self.root.left.left = BTNode(1)
        self.root.left.right = BTNode(3)

        self.assertEqual(closest_bst_value_iterative(self.root, 3.714286), 4)


if __name__ == "__main__":
    unittest.main()
