import unittest
from single_cycle_check import single_cycle_check

class TestSingleCycleCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.arrays = [[2, 3, 1, -4, -4, 2], [2, 2, -1], [2, 2, 2], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1], [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]]
        self.answers = [True, True, True, True, False, False, False]

    def test_generic(self):
        for idx, ans in enumerate(self.answers):
            self.assertEqual(ans, single_cycle_check(self.arrays[idx]))

if __name__ == "__main__": unittest.main()