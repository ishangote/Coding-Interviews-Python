import unittest


def find_first_and_last_position(nums, target):
    lo, hi = 0, len(nums) - 1
    res = [-1, -1]

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    if nums[lo] != target:
        return [-1, -1]

    res[0] = lo
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1

        else:
            hi = mid

    res[1] = hi

    return res


class TestFirstAndLastPositionOfElementInSortedArray(unittest.TestCase):
    def test_find_first_and_last_position(self):
        pass
