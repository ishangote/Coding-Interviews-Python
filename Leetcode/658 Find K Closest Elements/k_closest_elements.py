import unittest
import sys


def binary_search_helper(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo


# Time: O(logn + k), where n => length of arr
# Space: O(k)
def k_closest_elements(arr, target, k):
    pivot = binary_search_helper(arr, target)
    left, right = pivot - 1, pivot

    while k > 0:
        distance_left = target - arr[left] if left >= 0 else sys.maxsize
        distance_right = arr[right] - target if right < len(arr) else sys.maxsize

        if distance_left <= distance_right:
            left -= 1
        else:
            right += 1

        k -= 1

    return arr[left + 1 : right]


class TestKClosestElements(unittest.TestCase):
    def test_target_present(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        k = 4
        # Expected: Closest elements to 3 are [1, 2, 3, 4]
        self.assertEqual(k_closest_elements(arr, target, k), [1, 2, 3, 4])

    def test_target_absent(self):
        arr = [1, 2, 4, 5, 6]
        target = 3
        k = 4
        # Expected: For target 3, distances:
        # 1 -> 2, 2 -> 1, 4 -> 1, 5 -> 2, 6 -> 3
        # In tie (distance 1: 2 and 4), choose the left (2), so result is [1, 2, 4, 5]
        self.assertEqual(k_closest_elements(arr, target, k), [1, 2, 4, 5])

    def test_k_equals_length(self):
        arr = [1, 3, 5, 7, 9]
        target = 6
        k = 5
        # When k equals the array length, return the entire array.
        self.assertEqual(k_closest_elements(arr, target, k), [1, 3, 5, 7, 9])

    def test_single_element(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        k = 1
        # Expected: Only the element 3 is closest to 3.
        self.assertEqual(k_closest_elements(arr, target, k), [3])

    def test_tie_breaker(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        k = 2
        # For target 3, if tie between 2 and 4 (both distance 1),
        # tie-breaker rule picks the smaller element (2). The window should be [2, 3].
        self.assertEqual(k_closest_elements(arr, target, k), [2, 3])


if __name__ == "__main__":
    unittest.main()
