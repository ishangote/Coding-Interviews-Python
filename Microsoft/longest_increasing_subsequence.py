"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

"""
Brute Force: O(2^n)
[10,9,2,5,3,7,101,18]

10 9
10 2
10 5
...

Approach 2:
[2, 3, 1, 2 10, 7, 10]
                   i
                   j
[1, 2, 1, 2 3,  3, 4]

"""
def longest_increasing_subsequence(nums):
    memo = [1 for itr in range(len(nums)]
    for j in range(1, len(nums)):
        i = 0
        while i < j:
            if nums[j] > nums[i]: memo[j] = max(memo[j], memo[i] + 1)
            i += 1
    return max(memo)

"""
 0  1   2  3
[3, 1, -1, 2]
        i  j
[1, 1, 1,  2]
 ^
"""