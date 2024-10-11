import unittest
from collections import deque


class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Time: O(n), where n => number of nodes in BT
# Space: O(m), where m => maximum number of nodes at any level
def average_of_levels(root):
    queue = deque([(root, 0)])
    res = []

    while queue:
        node, level = queue.pop()

        if level == len(res):
            res.append([node.value])
        else:
            res[level].append(node.value)

        if node.left:
            queue.appendleft((node.left, level + 1))

        if node.right:
            queue.appendleft((node.right, level + 1))

    return list(map(lambda x: sum(x) / len(x), res))


class TestAverageOfLevels(unittest.TestCase):
    def test_average_of_levels(self):
        root = BTNode(3)

        root.left = BTNode(9)
        root.right = BTNode(20)

        root.right.left = BTNode(15)
        root.right.right = BTNode(7)

        self.assertEqual(average_of_levels(root), [3, 14.5, 11])


if __name__ == "__main__":
    unittest.main()
