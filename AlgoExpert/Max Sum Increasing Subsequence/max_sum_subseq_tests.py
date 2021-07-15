import unittest
from max_sum_subseq import maxSumIncreasingSubsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[8, 12, 2, 3, 15, 5, 7], [-1], [5, 4, 3, 2, 1], [10, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [10, 70, 20, 30, 50, 11, 30]]
        self.max_sum_subseq = [[35, [8, 12, 15]], [-1, [-1]], [5, [5]], [45, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [1]], [110, [10, 20, 30, 50]]]
        return super().setUp()
    
    def test_generic(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.max_sum_subseq[idx], maxSumIncreasingSubsequence(self.arrays[idx]))

if __name__ == "__main__": unittest.main()