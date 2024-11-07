import unittest


class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# Time: O(n), where n => number of nodes in BT
# Space: O(1)
def lowest_common_ancestor_iii(node1, node2):
    pt1, pt2 = node1, node2
    node1_height, node2_height = 0, 0

    while pt1.parent:
        node1_height += 1
        pt1 = pt1.parent

    while pt2.parent:
        node2_height += 1
        pt2 = pt2.parent

    pt1, pt2 = node1, node2

    while node1_height > node2_height:
        pt1 = pt1.parent
        node1_height -= 1

    while node1_height < node2_height:
        pt2 = pt2.parent
        node2_height -= 1

    while pt1 != pt2:
        pt1 = pt1.parent
        pt2 = pt2.parent

    return pt1


class TestLowestCommonAncestorIII(unittest.TestCase):
    def test_lowest_common_ancestor_iii(self):
        root = BTNode(3)
        root.parent = None

        root.left = BTNode(6)
        root.left.parent = root
        root.right = BTNode(8)
        root.right.parent = root

        node1 = root.left.left = BTNode(2)
        root.left.left.parent = root.left
        node2 = root.left.right = BTNode(11)
        root.left.right.parent = root.left

        root.right.right = BTNode(13)
        root.right.right.parent = root.right

        root.left.right.left = BTNode(9)
        root.left.right.left.parent = root.left.right
        root.left.right.right = BTNode(5)
        root.left.right.right.parent = root.left.right

        root.right.right.left = BTNode(7)
        root.right.right.left.parent = root.right.right

        self.assertEqual(lowest_common_ancestor_iii(node1, node2).value, 6)


if __name__ == "__main__":
    unittest.main()
