import unittest
from two_number_sum_naive import twoNumberSumNaive
from two_number_sum_sort import twoNumberSumSort
from two_number_sum_hm import twoNumberSumHM

class TestTwoSum(unittest.TestCase):
    def test_two_sum_generic(self):
        output = twoNumberSumNaive([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)

        output = twoNumberSumSort([4, 6, 1, -3], 3)
        self.assertTrue(len(output) == 2)
        self.assertTrue(6 in output)
        self.assertTrue(-3 in output)

        output = twoNumberSumHM([2, 3], 4)
        self.assertTrue(len(output) == 0)

if __name__ == "__main__": unittest.main()