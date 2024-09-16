# Time: O(log(n)), where n => length of nums
# Space: O(1)
def search_insert_position(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target < nums[mid]: hi = mid - 1
        elif target > nums[mid]: lo = mid + 1
        else: return mid

    return lo

import unittest
class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert_position(self):
        self.assertEqual(search_insert_position([1, 3, 5, 6], 0), 0)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 5), 2)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 2), 1)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 7), 4)

if __name__ == "__main__": unittest.main()
