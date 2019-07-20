# Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.
"""
**Example: **
For the given array [1 11 2 10 4 5 2 1]
Longest subsequence is [1 2 10 4 2 1]

Return value 6
"""

def longest_inc_dec_subseq(arr):
    if not arr: return 0
    
    inc_memo, dec_memo = [1] *len(arr), [1] *len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]: inc_memo[i] = max(inc_memo[i], inc_memo[j] + 1)
    
    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            