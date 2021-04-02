"""
Given an array of integers A, return the largest integer that only occurs once.
If no integer occurs once, return -1.

Example 1:
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Example 2:
Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 
Note:
1 <= A.length <= 2000
0 <= A[i] <= 1000
"""

"""
Questions: 
1. What if there are no unique nums? -> return -1
2. Is the array sorted? -> Not necessary
3. nums -ve? no 


Examples: 
A =
[5, 7, 8, 9, 7, 9, 9]

sort A =
[5, 7, 7, 8, 9, 9, 9]
                c
max_val = 9
cur == max_val => max_val -1
cur > max_val => max_val = cur
cur < max_val => return max_val
ans =
8

--------------

A = 
[0]
c
max_val = 0

Time: O(nlogn)
Space: O(1)
"""

def largest_unique_number_naive(A):
    A.sort()
    max_val = -1
    cur_idx = len(A) - 1
    while cur_idx > -1:
        if A[cur_idx] == max_val:
            while cur_idx > -1 and A[cur_idx] == max_val:
                cur_idx -= 1
            max_val = -1

        elif A[cur_idx] > max_val: 
            max_val = A[cur_idx]
            cur_idx -= 1

        else: return max_val
    return max_val