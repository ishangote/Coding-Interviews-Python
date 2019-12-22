#Given an integer array nums, find the contiguous subarray (containing at least one number) 
#which has the largest sum and return its sum.

"""
max(prev_sum + nums[idx], nums[idx])

 0   1   2  3   4  5  6   7  8  
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

dp
[-2, 1, -2, 4, 3, 5, 6, 1, 4]

return 6

"""
import unittest
def kadane(nums):
    if not nums: return 0
    ans = curr_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        ans = max(ans, curr_sum)
    return ans
    
class TestKadanesAlgorithm(unittest.TestCase):
    def test_null_array(self):
        self.assertEqual(kadane([]), 0)

    def test_all_negative_array(self):
        self.assertEqual(kadane([-5, -3, -12, -5, -3]), -3)

    def test_one_element(self):
        self.assertEqual(kadane([3]), 3)

    def test_mixed_array(self):
        self.assertEqual(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(kadane([-3, 1, 0, -2, 3, 4, -1, 4, -2]), 10)
        self.assertEqual(kadane([9, 8, -1, -2, -3]), 17)

if __name__ == "__main__": unittest.main()