import unittest
from three_number_sum_naive import three_sum_naive
from three_number_sum_hash_map import three_sum_hm
from three_number_sum_two_pointers import three_sum_two_pointers

class TestThreeSum(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(three_sum_naive([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
        self.assertEqual(three_sum_hm([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
        self.assertEqual(three_sum_two_pointers([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

if __name__ == "__main__": unittest.main()