import unittest
import sys


# Time: O(n + k), where n => length of arr
# Space: O(1)
def kth_missing_positive_number_linear_search(arr, k):
    idx = 0
    missing_count = 0

    for num in range(1, len(arr) + k + 1):
        if idx < len(arr) and arr[idx] == num:
            idx += 1
        else:
            missing_count += 1
            if missing_count == k:
                return num


# TODO:
def kth_missing_positive_number_binary_search(arr, k):
    pass


class TestKthPositiveNumber(unittest.TestCase):
    def test_kth_missing_positive_number_linear_search(self):
        self.assertEqual(
            kth_missing_positive_number_linear_search([1, 2, 3, 4, 5], 2), 7
        )
        self.assertEqual(kth_missing_positive_number_linear_search([5, 6, 7, 8], 2), 2)
        self.assertEqual(
            kth_missing_positive_number_linear_search([1, 2, 3, 5, 9], 2), 6
        )
        self.assertEqual(
            kth_missing_positive_number_linear_search([1, 2, 3, 7, 9], 2), 5
        )


if __name__ == "__main__":
    unittest.main()
