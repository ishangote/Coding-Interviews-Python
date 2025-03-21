import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def find_pivot_index(nums):
    left_sum = [-1 for _ in range(len(nums))]
    right_sum = [-1 for _ in range(len(nums))]

    cur_sum = 0
    for idx in range(len(nums)):
        cur_sum += nums[idx]
        left_sum[idx] = cur_sum

    cur_sum = 0
    for idx in range(len(nums) - 1, -1, -1):
        cur_sum += nums[idx]
        right_sum[idx] = cur_sum

    for idx in range(len(nums)):
        if left_sum[idx] != right_sum[idx]:
            continue
        return idx

    return -1


# Time: O(n), where n => length of nums
# Space: O(1)
def find_pivot_optimized(nums):
    total_sum = sum(nums)
    prefix_sum = 0

    for idx in range(len(nums)):
        suffix_sum = total_sum - prefix_sum - nums[idx]

        if prefix_sum == suffix_sum:
            return idx

        prefix_sum += nums[idx]

    return -1


class TestFindPivotIndex(unittest.TestCase):
    def test_find_pivot_index(self):
        self.assertEqual(find_pivot_index([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(find_pivot_index([1, 2, 3]), -1)
        self.assertEqual(find_pivot_index([2, 1, -1]), 0)

    def test_find_pivot_index_optimized(self):
        self.assertEqual(find_pivot_optimized([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(find_pivot_optimized([1, 2, 3]), -1)
        self.assertEqual(find_pivot_optimized([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
