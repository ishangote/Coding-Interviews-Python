import unittest


class NTNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def recursive_helper(node, res):
    if not node:
        return 0

    max_height1, max_height2 = 0, 0

    for child_node in node.children:
        child_height = recursive_helper(child_node, res)
        if child_height > max_height1:
            max_height2 = max_height1
            max_height1 = child_height

        elif child_height > max_height2:
            max_height2 = child_height

    res[0] = max(res[0], max_height1 + max_height2)
    return 1 + max_height1


# Time: O(n), where n => number of nodes in NT
# Space: O(n)
def diameter_of_nary_tree(root):
    res = [0]
    recursive_helper(root, res)
    return res[0]


class TestNaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        """Set up test cases by constructing sample N-ary trees"""

        # Test Case 1: Single Node Tree
        self.tree1 = NTNode(1)

        # Test Case 2: Three-Level Balanced Tree
        self.tree2 = NTNode(1)
        self.tree2.children = [NTNode(2), NTNode(3), NTNode(4)]
        self.tree2.children[0].children = [NTNode(5), NTNode(6)]
        self.tree2.children[1].children = [NTNode(7)]
        self.tree2.children[2].children = [NTNode(8), NTNode(9)]

        # Test Case 3: Unbalanced Tree
        self.tree3 = NTNode(1)
        self.tree3.children = [NTNode(2)]
        self.tree3.children[0].children = [NTNode(3)]
        self.tree3.children[0].children[0].children = [NTNode(4)]
        self.tree3.children[0].children[0].children[0].children = [NTNode(5)]

    def test_single_node(self):
        """Diameter of a single node tree should be 0"""
        self.assertEqual(diameter_of_nary_tree(self.tree1), 0)

    def test_balanced_tree(self):
        """Test a balanced N-ary tree"""
        self.assertEqual(
            diameter_of_nary_tree(self.tree2), 4
        )  # Longest path: 5 → 2 → 1 → 4 → 9

    def test_unbalanced_tree(self):
        """Test an unbalanced tree where longest path is down a single branch"""
        self.assertEqual(
            diameter_of_nary_tree(self.tree3), 4
        )  # Longest path: 1 → 2 → 3 → 4 → 5


if __name__ == "__main__":
    unittest.main()
