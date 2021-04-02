# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.

"""
Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""

"""
Questions:
1. No susch subset? return 0
2. Subset non contiguous? yes

Examples:
Brute Force: 
1. Generate all subsets
2. Check conditions for each subset
3. return max len

Time: O(2^n * l), n = len(strs), l = max length of string in strs
Space: O(2^n * l)

Input: 
strs = ["10","0001","111001","1","0"], m = 5, n = 3 (m -> 0s, n -> 1s)
          ^
count_0 = 5
count_1 = 3
subset = ["10", "0001", "1", "0"]
Output: 4

-----------------------

Input: 
strs = 
["10","0","1"], m = 1, n = 1
Output: 2

recursive subset generation brute force => 

go left => accept the number
go right => reject the number

                                                    []
                            ["10"]                                           []
            ["10", "0"]                   ["10"]                    ["0"]                   []
["10", "0", "1"]   ["10", "0"]    ["10", "1"]  ["10"]      ["0", "1"]   ["0"]          ["1"]   []

"""
def get_counts(s):
    zeroes, ones = 0, 0
    for num in s:
        if num == "0": zeroes += 1
        else: ones += 1
    return [zeroes, ones]

def ones_and_zeroes_naive(strs, m, n):
    return ones_zeroes_helper(strs, m, n, 0)

def ones_zeroes_helper(strs, zeroes, ones, idx):
    #Break condition
    if idx == len(strs) or zeroes + ones == 0: return 0
    
    count0, count1 = get_counts(strs[idx])
    accept = 0
    if count0 <= zeroes and count1 <= ones:
        accept = 1 + ones_zeroes_helper(strs, zeroes - count0, ones - count1, idx + 1)
    
    reject = ones_zeroes_helper(strs, zeroes, ones, idx + 1)
    
    return max(accept, reject)