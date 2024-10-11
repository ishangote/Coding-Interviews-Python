import sys
import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def maximum_average_sum_i_while(nums, k):
    max_cur_sum = cur_sum = sum(nums[:k])

    lo, hi = 1, k

    while lo < len(nums) and hi < len(nums):
        cur_sum = cur_sum - nums[lo - 1] + nums[hi]
        max_cur_sum = max(max_cur_sum, cur_sum)

        lo += 1
        hi += 1

    return max_cur_sum / k


# Time: O(n), where n => length of nums
# Space: O(1)
def maximum_average_sum_i_for(nums, k):
    max_cur_sum = cur_sum = -sys.maxsize

    for idx in range(len(nums) - k + 1):
        if idx == 0:
            cur_sum = sum(nums[0:k])

        else:
            cur_sum = cur_sum - nums[idx - 1] + nums[idx + k - 1]

        max_cur_sum = max(max_cur_sum, cur_sum)

    return max_cur_sum / k


class TestMaximumAverageSumI(unittest.TestCase):
    def test_maximum_average_sum_i_while(self):
        self.assertEqual(maximum_average_sum_i_while([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(maximum_average_sum_i_while([5], 1), 5)

    def test_maximum_average_sum_i_for(self):
        self.assertEqual(maximum_average_sum_i_for([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(maximum_average_sum_i_for([5], 1), 5)
        self.assertEqual(maximum_average_sum_i_for([-1], 1), -1)


if __name__ == "__main__":
    unittest.main()
