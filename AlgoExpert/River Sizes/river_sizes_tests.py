import unittest
from river_sizes import get_river_sizes

class TestRiverSizes(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [[[1, 0, 0, 1, 0],[1, 0, 1, 0, 0],[0, 0, 1, 0, 1],[1, 0, 1, 0, 1],[1, 0, 1, 1, 0]], [[1, 1, 0],[1, 0, 1],[1, 1, 1],[1, 1, 0],[1, 0, 1],[0, 1, 0],[1, 0, 0],[1, 0, 0],[0, 0, 0],[1, 0, 0],[1, 0, 1],[1, 1, 1]], [[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],[1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],[0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],[1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],[1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]]
        self.sizes = [[2, 1, 5, 2, 2], [10, 1, 1, 2, 6], [2, 1, 21, 5, 2, 1]]
    
    def test_generic(self):
        for idx, size in enumerate(self.sizes):
            self.assertEqual(size, get_river_sizes(self.matrix[idx]))

if __name__ == "__main__": unittest.main()