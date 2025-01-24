import unittest


class DSNode:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


class DisjointSet:
    def __init__(self):
        self.node_map = {}

    def make_set(self, value):
        if value not in self.node_map:
            self.node_map[value] = DSNode(value)

    def union(self, value1, value2):
        node1, node2 = self.node_map[value1], self.node_map[value2]

        root1 = self.find_set_node(node1)
        root2 = self.find_set_node(node2)

        if root1 == root2:
            return

        if root1.rank > root2.rank:
            root2.parent = root1
        elif root1.rank < root2.rank:
            root1.parent = root2
        else:
            root2.parent = root1
            root1.rank += 1

    def find_set(self, value):
        node = self.node_map[value]
        root = self.find_set_node(node)
        return root.value

    def find_set_node(self, node):
        if node.parent != node:
            node.parent = self.find_set_node(node.parent)

        return node.parent


# Time: O(klogk + n + k⋅α(n)) ~ O(klogk + n), where k => number of logs, n => number of persons
# Space: O(k + n)
def earliest_friends(logs, n):
    logs = sorted(logs, key=lambda x: x[0])

    ds = DisjointSet()
    connected_components = n

    for person in range(n):
        ds.make_set(person)

    for log in logs:
        time, person1, person2 = log

        # If persons are already friends, ignore
        if ds.find_set(person1) == ds.find_set(person2):
            continue

        ds.union(person1, person2)
        connected_components -= 1

        if connected_components == 1:
            return time

    return -1


class TestEarliestFriends(unittest.TestCase):
    def test_earliest_friends(self):
        self.assertEqual(
            earliest_friends(
                [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4
            ),
            3,
        )
        self.assertEqual(
            earliest_friends(
                [
                    [20190101, 0, 1],
                    [20190104, 3, 4],
                    [20190107, 2, 3],
                    [20190211, 1, 5],
                    [20190224, 2, 4],
                    [20190301, 0, 3],
                    [20190312, 1, 2],
                    [20190322, 4, 5],
                ],
                6,
            ),
            20190301,
        )


if __name__ == "__main__":
    unittest.main()
