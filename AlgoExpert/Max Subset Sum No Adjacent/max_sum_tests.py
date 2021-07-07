import unittest
from max_sum import *
class TestMaxSubsetSumNoAdjacent(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[75, 105, 120, 75, 90, 135], [], [1], [1, 2], [1, 2, 3], [1, 15, 3], [7, 10, 12, 7, 9, 14], [4, 3, 5, 200, 5, 3], [10, 5, 20, 25, 15, 5, 5, 15], [10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15]]
        self.answers = [330, 0, 1, 2, 4, 15, 33, 207, 60, 90]
    
    def test_naive(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.answers[idx], max_sum_naive(arr))
    
    def test_optim(self):
        for idx, arr in enumerate(self.arrays):
            self.assertEqual(self.answers[idx], max_sum_optim(arr))

if __name__ == "__main__": unittest.main()