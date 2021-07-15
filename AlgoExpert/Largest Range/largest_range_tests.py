import unittest
from largest_range import largestRangeNaive, largestRangeOptim

class TestLargestRange(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6], [10, 0, 1], [0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2], [4, 2, 1, 3], [8, 4, 2, 10, 3, 6, 7, 9, 1], [1]]
        self.ranges = [[0, 7], [0, 1], [-7, 7], [1, 4], [6, 10], [1, 1]]
        return super().setUp()
    
    def test_naive(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.ranges[idx], largestRangeNaive(self.arrays[idx]))
    
    def test_optim(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.ranges[idx], largestRangeOptim(self.arrays[idx]))

if __name__ == "__main__": unittest.main()