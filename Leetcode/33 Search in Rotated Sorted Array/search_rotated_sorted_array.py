import unittest


def search_pivot(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid - 1] > nums[mid]:
            return mid
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


def search_target(pivot, nums, target):
    (lo, hi) = (
        (pivot, len(nums) - 1) if nums[pivot] <= target <= nums[-1] else (0, pivot - 1)
    )

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


# Time: O(log(n)), where n => length of nums
# Space: O(1)
def search_rotated_sorted_array(nums, target):
    pivot = search_pivot(nums)
    return search_target(pivot, target, nums)


class TestShiftedArraySearch(unittest.TestCase):
    def test_search_rotated_sorted_array(self):
        self.assertEqual(search_rotated_sorted_array([2], 2), 0)
        self.assertEqual(search_rotated_sorted_array([2, 6, 8, 11], 6), 1)
        self.assertEqual(search_rotated_sorted_array([9, 12, 17, 2, 4, 5], 2), 3)
        self.assertEqual(search_rotated_sorted_array([9, 12, 17, 2, 4, 5], 13), -1)


if __name__ == "__main__":
    unittest.main()
