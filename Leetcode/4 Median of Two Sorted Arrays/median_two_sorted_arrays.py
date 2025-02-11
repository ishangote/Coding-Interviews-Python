import unittest
import sys


# Time: O(log(min(x, y))), where x, y => lengths of input arrays
# Space: O(1)
def median_of_two_sorted_arrays(arr_x, arr_y):
    if len(arr_x) > len(arr_y):
        arr_x, arr_y = arr_y, arr_x

    lo, hi = 0, len(arr_x)
    total_length = len(arr_x) + len(arr_y)

    while lo <= hi:
        partition_x = (lo + hi) // 2
        # (total_length + 1) ensures the left partition has one more element than the right when the total length is odd.
        partition_y = (total_length + 1) // 2 - partition_x

        left_x = -sys.maxsize if partition_x == 0 else arr_x[partition_x - 1]
        left_y = -sys.maxsize if partition_y == 0 else arr_y[partition_y - 1]

        right_x = sys.maxsize if partition_x == len(arr_x) else arr_x[partition_x]
        right_y = sys.maxsize if partition_y == len(arr_y) else arr_y[partition_y]

        if left_x <= right_y and left_y <= right_x:
            if total_length % 2 == 0:
                return (max(left_x, left_y) + min(right_x, right_y)) / 2
            else:
                return max(left_x, left_y)

        if left_x > right_y:
            hi = partition_x - 1
        else:
            lo = partition_x + 1

    raise ValueError("Input arrays are not sorted or invalid.")


class MedianOfTwoSortedArrays(unittest.TestCase):
    def test_median_of_two_sorted_arrays(self):
        self.assertEqual(
            median_of_two_sorted_arrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]), 11
        )
        self.assertEqual(median_of_two_sorted_arrays([1, 3], [2]), 2)
        self.assertEqual(median_of_two_sorted_arrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(median_of_two_sorted_arrays([], [1]), 1)
        self.assertEqual(median_of_two_sorted_arrays([2], [1]), 1.5)
        self.assertEqual(median_of_two_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]), 4.5)


if __name__ == "__main__":
    unittest.main()
