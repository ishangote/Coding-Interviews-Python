import unittest


# Time: O(n^2), where n => length of nums
# Space: O(1)
def sum_of_subarray_ranges_brute_force(nums):
    res = 0

    for idx1 in range(len(nums) - 1):
        min_num, max_num = nums[idx1], nums[idx1]

        for idx2 in range(idx1 + 1, len(nums)):
            max_num = max(max_num, nums[idx2])
            min_num = min(min_num, nums[idx2])

            res += max_num - min_num

    return res


# ------------------------------------------------------- #


def sum_of_subarray_maximums(nums):
    def previous_greater_or_equal_indices():
        res = [-1] * len(nums)
        stack = []

        for idx in range(len(nums) - 1, -1, -1):
            while stack and nums[idx] >= nums[stack[-1]]:
                index = stack.pop()
                res[index] = idx

            stack.append(idx)

        return res

    def previous_greater_indices():
        res = [len(nums)] * len(nums)
        stack = []

        for idx in range(len(nums)):
            while stack and nums[idx] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = idx

            stack.append(idx)

        return res

    prev_greater = previous_greater_or_equal_indices()
    next_greater = previous_greater_indices()

    res = sum(
        nums[idx] * (idx - prev_greater[idx]) * (next_greater[idx] - idx)
        for idx in range(len(nums))
    )

    return res


def sum_of_subarray_minimums(nums):
    def previous_smaller_or_equal_indices():
        res = [-1] * len(nums)
        stack = []

        for idx in range(len(nums) - 1, -1, -1):
            while stack and nums[idx] <= nums[stack[-1]]:
                index = stack.pop()
                res[index] = idx

            stack.append(idx)

        return res

    def next_smaller_indices():
        res = [len(nums)] * len(nums)
        stack = []

        for idx in range(len(nums)):
            while stack and nums[idx] < nums[stack[-1]]:
                index = stack.pop()
                res[index] = idx

            stack.append(idx)

        return res

    prev_smaller = previous_smaller_or_equal_indices()
    next_smaller = next_smaller_indices()

    res = sum(
        nums[idx] * (idx - prev_smaller[idx]) * (next_smaller[idx] - idx)
        for idx in range(len(nums))
    )

    return res


def sum_of_subarray_ranges_mono(nums):
    sum_of_maximums = sum_of_subarray_maximums(nums)
    sum_of_minimums = sum_of_subarray_minimums(nums)

    return sum_of_maximums - sum_of_minimums


class TestSumOfSubArrayRanges(unittest.TestCase):
    def test_sum_of_subarray_ranges_brute_force(self):
        self.assertEqual(sum_of_subarray_ranges_brute_force([1, 2, 3]), 4)
        self.assertEqual(sum_of_subarray_ranges_brute_force([1, 3, 3]), 4)
        self.assertEqual(sum_of_subarray_ranges_brute_force([4, -2, -3, 4, 1]), 59)

    def test_sum_of_subarray_ranges_mono(self):
        self.assertEqual(sum_of_subarray_ranges_mono([1, 2, 3]), 4)
        self.assertEqual(sum_of_subarray_ranges_mono([1, 3, 3]), 4)
        self.assertEqual(sum_of_subarray_ranges_mono([4, -2, -3, 4, 1]), 59)


if __name__ == "__main__":
    unittest.main()
