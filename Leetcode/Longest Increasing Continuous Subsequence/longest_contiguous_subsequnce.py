# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

def longest_contiguous_subsequence(nums):
    start, ans = 0, 0
    for i in range(len(nums)):
        if i != 0 and nums[i - 1] >= nums[i]: start = i
        ans = max(ans, i - start + 1)
    return ans

import unittest
class TestLongestContinuousSubsequence(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(longest_contiguous_subsequence([1,3,5,4,7]), 3)
        self.assertEqual(longest_contiguous_subsequence([2,2,2,2,2]), 1)

if __name__ == "__main__": unittest.main()