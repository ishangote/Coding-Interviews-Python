import unittest
import sys


# Time: O(n), where n => length of nums
# Space: O(n)
def largest_outlier_in_array(nums):
    max_outlier = None
    index_map = {num: idx for idx, num in enumerate(nums)}
    total_sum = sum(nums)

    for idx, outlier in enumerate(nums):
        remaining_sum = total_sum - outlier
        if (
            remaining_sum % 2 == 0
            and remaining_sum // 2 in index_map
            and index_map[remaining_sum // 2] != idx
        ):
            max_outlier = max(max_outlier, outlier) if max_outlier else outlier

    return max_outlier


class TestLargestOutlierInArray(unittest.TestCase):
    def test_largest_outlier_in_array(self):
        self.assertEqual(largest_outlier_in_array([2, 3, 5, 10]), 10)
        self.assertEqual(largest_outlier_in_array([-2, -1, -3, -6, 4]), 4)
        self.assertEqual(largest_outlier_in_array([1, 1, 1, 1, 1, 5, 5]), 5)


if __name__ == "__main__":
    unittest.main()
