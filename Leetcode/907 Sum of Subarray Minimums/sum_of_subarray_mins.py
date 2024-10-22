import unittest


# Time: O(n^2), where n => length of nums
# Space: O(1)
def sum_of_subarray_minimums_brute_force(nums):
    res = 0

    for idx1 in range(len(nums)):
        current_min = nums[idx1]
        for idx2 in range(idx1, len(nums)):
            current_min = min(current_min, nums[idx2])
            res += current_min
            res %= 10**9 + 7

    return res


# ------------------------------------------------------ #


# * Problem: Previous Smaller
# * Direction: Right to Left
# * Stack Type: Increasing
def previous_smaller_or_equal_indices(nums):
    res = [-1] * len(nums)
    stack = []

    for idx in range(len(nums) - 1, -1, -1):
        while stack and nums[idx] <= nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


# * Problem: Next Smaller
# * Direction: Left to Right
# * Stack Type: Increasing
def next_smaller_indices(nums):
    res = [len(nums)] * len(nums)
    stack = []

    for idx in range(len(nums)):
        while stack and nums[idx] < nums[stack[-1]]:
            index = stack.pop()
            res[index] = idx

        stack.append(idx)

    return res


# Time: O(n), where n => length of nums
# Space: O(n)
def sum_of_subarray_minimums_mono(nums):
    prev_smaller = previous_smaller_or_equal_indices(nums)
    next_smaller = next_smaller_indices(nums)

    res = sum(
        nums[idx] * (idx - prev_smaller[idx]) * (next_smaller[idx] - idx)
        for idx in range(len(nums))
    ) % (10**9 + 7)

    return res


class TestSumOfSubarrayMinimums(unittest.TestCase):
    def test_previous_smaller_indices(self):
        self.assertListEqual(
            previous_smaller_or_equal_indices([3, 1, 2, 4]), [-1, -1, 1, 2]
        )
        self.assertListEqual(
            previous_smaller_or_equal_indices([71, 55, 82, 55]), [-1, -1, 1, 1]
        )

    def test_next_smaller_indices(self):
        self.assertListEqual(next_smaller_indices([71, 55, 82, 55]), [1, 4, 3, 4])

    def test_sum_of_subarray_minimums_brute_force(self):
        self.assertEqual(sum_of_subarray_minimums_brute_force([3, 1, 2, 4]), 17)

    def test_sum_of_subarray_minimums_mono(self):
        self.assertEqual(sum_of_subarray_minimums_mono([3, 1, 2, 4]), 17)
        self.assertEqual(sum_of_subarray_minimums_mono([71, 55, 82, 55]), 593)


"""               0   1   2   3
nums =          [71, 55, 82, 55]
                     ^
prev_small =    [-1, -1, 1, 1]
next_small =    [1, 3, 3, 4]

res = 

71 * 1 * 1
55 * 1 * 2
82 * 1 * 1
55 * (3 - (1 + 1) + 1) * 1=> 55 * 2 * 1     => INCORRECT
...

* avoid duplicated count of repeated minimums *

How do you rationalize the different condition for left and right?

# previous smaller
while stack and nums[idx] <= nums[stack[-1]]:

# next smaller
while stack and nums[idx] < nums[stack[-1]]:

To avoid counting the same subarray multiple times, we uniquely identify each subarray by its [left_end_point, right_end_point]. 
Two pairs are considered different if either the left or right endpoint differs. 
To ensure this, we use one >= and one >. This prevents duplicates by ensuring each subarray's boundaries are distinct. 
Using two > or two >= would fail to differentiate some subarrays properly.
"""

if __name__ == "__main__":
    unittest.main()
