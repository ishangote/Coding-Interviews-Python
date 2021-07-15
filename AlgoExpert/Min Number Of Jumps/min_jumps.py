"""
Questions:
1. What if we can not reach the end? 
2. Only positive integers in array? yes

Examples:
array = 
 0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 
[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

Idea:
min_jums_to_reach_10 = 1 + min(min_jums_to_reach_0, min_jumps_to_reach_1, min_jumps_to_reach_2, ... min_jumps_to_reach_9)
min_jumps_to_reach_0 = 0

array = 
 0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 
[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
                               i
                            j
jumps = 
[0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4]

return jumps[-1] = 4

Time: O(n^2)
Space:O(n)

---------------------------------

array = 
 0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 
[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

                                0 {3}
                        1{4}   2{2}   3{1}
                2{2} 3{1} 4{2} 5{3} ...

if idx >= len(array) - 1: return 0
memo[idx] => stores min distance between idx and len(array) - 1

Time: O(n)
Space: O(n)
"""

import sys
def min_jumps_dp(array):
    jumps = [0] + [sys.maxsize] * (len(array) - 1)
    
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] >= i - j:
                jumps[i] = min(jumps[i], 1 + jumps[j])
    return jumps[-1]

#----------------------------------

def min_jumps_helper(array, idx, memo):
    if idx in memo: return memo[idx]
    if idx >= len(array) - 1: memo[idx] = 0
    else:
        memo[idx] = float('inf')
        for i in range(1, array[idx] + 1):
            memo[idx] = min(memo[idx], 1 + min_jumps_helper(array, idx + i, memo))
    return memo[idx]

def min_jumps_recur(array):
    memo = {}
    return min_jumps_helper(array, 0, memo)