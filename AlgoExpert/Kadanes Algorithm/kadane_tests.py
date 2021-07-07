import unittest
from kadane import *

class TestKadane(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5], [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, -22, 7, 8, 9, 10], [3, 4, -6, 7, 8, -18, 100], [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 6], [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]]
        self.sums = [19, 55, -1, -1, 35, 34, 100, 24, 6]

    def test_naive(self):
        for idx, sum in enumerate(self.sums):
            self.assertEqual(sum, naive(self.arrays[idx]))
    
    def test_optim(self):
        for idx, sum in enumerate(self.sums):
            self.assertEqual(sum, kadane_optim(self.arrays[idx]))

    def test_space_optim(self):
        for idx, sum in enumerate(self.sums):
            self.assertEqual(sum, kadane_space_optim(self.arrays[idx]))

if __name__ == "__main__": unittest.main()