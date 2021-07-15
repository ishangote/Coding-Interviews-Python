import unittest
from min_jumps import min_jumps_dp, min_jumps_recur

class TestMinJumps(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[5, 1, 1, 1, 1, 1], [3, 1], [2, 1, 2, 3, 1, 1, 1], [3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1], [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3], [3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]]
        self.min_jumps = [1, 1, 3, 3, 4, 5]
        return super().setUp()

    def test_generic_dp(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.min_jumps[idx], min_jumps_dp(self.arrays[idx]))

    def test_generic_recursion(self):
        for idx in range(len(self.arrays)):
            self.assertEqual(self.min_jumps[idx], min_jumps_recur(self.arrays[idx]))

if __name__ == "__main__": unittest.main()