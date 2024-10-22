import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def min_swaps_for_valid_array(nums):
    min_num = min(nums)
    min_idx = nums.index(min_num)

    nums = [min_num] + nums[:min_idx] + nums[min_idx + 1 :]

    max_num = max(nums)
    max_idx = nums[::-1].index(max_num)

    return min_idx + max_idx


class TestAdjacentSwapsToMakeValidArray(unittest.TestCase):
    def test_min_swaps_for_valid_array(self):
        self.assertEqual(min_swaps_for_valid_array([3, 4, 5, 5, 3, 1]), 6)
        self.assertEqual(min_swaps_for_valid_array([1]), 0)


if __name__ == "__main__":
    unittest.main()
