
# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
# that is, sums up to n*k where n is also an integer.
"""
Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Approach 1: O(n^3) Brute Force
Pseudo 1:
n -> len(arr)
for i -> [0, n - 1):
    for j -> [i + 1, n):
        if sum(i:j) % k == 0: return True  
return False

Approach 2: Better Brute Force O(n^2)
Pseudo 2:
n -> len(arr)
for i -> [0, n - 1):
    previous_sum = nums[i]
    for j -> [i + 1, n):
        if previous_sum + nums[j] % k == 0: return True
        else: previous_sum += nums[j]       
return False

Approach 3: Very intersting!
Theory:
return True if X % k == 0 where X is the sum of our subarray
Assume X = (a - b) where a and b are non negative int
if a % k = x
and if b % k = x
then
X % k = (a - b) % k = (x - x) % k = 0

[2, 5, 33, 6, 7, 25, 15], 13
           ^
           sum = 46 => 46 % 13 = 7
           7 is in hm
sum:idx
{
    2: 0
    7: 1
    40:3
}
"""
# O(n^2)
def continuous_subarray_sum(nums, k):
    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] == 0: return True
        return False

    for i in range(len(nums) - 1):
        prev_sum = nums[i]
        for j in range(i + 1, len(nums)):
            prev_sum += nums[j]
            if prev_sum % k == 0: return True
    return False

# O(n)
def continuous_subarray_sum_optimized(nums, k):
    
    hm = {0: -1}
    total = 0
    for i, v in enumerate(nums):
        total += v
        if k != 0:
            total %= k
        if total not in hm:
            hm[total] = i
        else:
            if i - hm[total] >= 2: return True
    
    return False        

import unittest
class TestContinuousSubarraySum(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(continuous_subarray_sum([5], 5), False)
        self.assertEqual(continuous_subarray_sum([5, 0, 0], 0), True)
        self.assertEqual(continuous_subarray_sum([0, 5, 0], 0), False)


        self.assertEqual(continuous_subarray_sum_optimized([5], 5), False)
        self.assertEqual(continuous_subarray_sum_optimized([5, 0, 0], 0), True)
        self.assertEqual(continuous_subarray_sum_optimized([0, 5, 0], 0), False)

    def test_generic(self):
        self.assertEqual(continuous_subarray_sum([23,2,6,4,7], 6), True)
        self.assertEqual(continuous_subarray_sum([23,2,4,6,7], -6), True)
        self.assertEqual(continuous_subarray_sum([0, 0], -1), True)
        self.assertEqual(continuous_subarray_sum([0, 1], -1), True)
        self.assertEqual(continuous_subarray_sum([0, 1, 0], -1), True)

        self.assertEqual(continuous_subarray_sum_optimized([23,2,6,4,7], 6), True)
        self.assertEqual(continuous_subarray_sum_optimized([23,2,4,6,7], -6), True)
        self.assertEqual(continuous_subarray_sum_optimized([0, 0], -1), True)
        self.assertEqual(continuous_subarray_sum_optimized([0, 1], -1), True)
        self.assertEqual(continuous_subarray_sum_optimized([0, 1, 0], -1), True)

if __name__ == "__main__": unittest.main()                