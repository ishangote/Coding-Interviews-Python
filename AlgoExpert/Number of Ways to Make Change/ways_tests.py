import unittest
from ways import number_of_ways
class TestNumberOfWaysToMakeChange(unittest.TestCase):
    def setUp(self) -> None:
        self.denoms = [[1, 5], [2, 3, 4, 7], [5], [2, 4], [1, 5, 10, 25], [1, 5, 10, 25], [1, 5, 10, 25]]
        self.targets = [6, 0, 9, 7, 4, 5, 10]
        self.ways = [2, 1, 0, 0, 1, 2, 4]

    def test_generic(self):
        for idx in range(len(self.denoms)):
            self.assertEqual(self.ways[idx], number_of_ways(self.targets[idx], self.denoms[idx]))

if __name__ == "__main__": unittest.main()                        