import unittest
from maximum_subarray import maximum_subarray
class TestMaximumSubarrayAlgorithm(unittest.TestCase):
    # def test_null_array(self):
    #     self.assertEqual(maximum_subarray([]), 0)

    def test_all_negative_array(self):
        self.assertEqual(maximum_subarray([-5, -3, -12, -5, -3]), -3)

    def test_one_element(self):
        self.assertEqual(maximum_subarray([3]), 3)

    def test_mixed_array(self):
        self.assertEqual(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maximum_subarray([-3, 1, 0, -2, 3, 4, -1, 4, -2]), 10)
        self.assertEqual(maximum_subarray([9, 8, -1, -2, -3]), 17)

if __name__ == "__main__": unittest.main()