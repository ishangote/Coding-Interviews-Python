# Given an unsorted array of integers, find the length of longest increasing subsequence.
"""
Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

Brute Force:  O(2^n) to find all subsequences as it is not continuous

Approach 1: Dynamic Prog

[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp

 j   i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] > arr[i] : j = 0  i+= 1

 j      i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] > arr[i] : j += 1  i

     j  i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] > arr[i] : j = 0  i

j          i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] > arr[i] : j += 1  i

     j     i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] > arr[i] : j += 1  i

        j  i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 1, 1, 1, 1,   1] dp
arr[j] < arr[i] : j += 1  i
dp[i] = max(dp[i], dp[j] + 1)

        j  i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 2, 1, 1, 1,   1] dp
arr[j] = arr[i] : j = 0  i += 1

j             i
[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 2, 1, 1, 1,   1] dp
arr[j] < arr[i] : j = 0  i += 1

"""
# O(n^2)
def longest_increasing_subsequence_dp(arr):
    if not arr: return 0
    
    memo = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] >= arr[j]: memo[i] = max(memo[i], memo[j] + 1)
    
    return max(memo)

import unittest
class TestLongestSubsequence(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(longest_increasing_subsequence_dp([]), 0)
    
    def test_generic_example(self):
        self.assertEqual(longest_increasing_subsequence_dp([3, 4, -1, 0, 6, 2, 3]), 4)
        self.assertEqual(longest_increasing_subsequence_dp([10,9,2,5,3,7,101,18]), 4)
        
if __name__ == "__main__": unittest.main()