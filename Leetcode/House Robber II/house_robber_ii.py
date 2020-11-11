# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

"""
Questions:
1. nums empty? -> return 0
2. Can house have zero money? -> Yes
3. Can house have negative money? -> No
4. Can we skip multiple houses in between? -> Yes

Examples:

 0  1  2
[2, 3, 2]

        2
    2       3

------------------------
 0  1  2  3  4
[1, 2, 0, 1, 3]

Can not rob house 0 2 4 since house 0 and 4 are adjacent => 
If robbed house 0, then can not rob house n - 1

 0  1  2  3  4  5
[1, 2, 0, 1, 3, 2]

Can rob 1 3 5 =>
If robbed house 1, then can rob house n - 1

So there are two choices =>
Rob houses [0:n - 1) or rob houses [1, n - 1] => return maximum of these two options

=>       0  1  2  3  4  5
house = [1, 2, 0, 1, 3, 2]
=>
rob_house([1, 2, 0, 1, 3])  or rob_house([2, 0, 1, 3, 2])

"""
# Time: O(n)
# Space: O(1)
def rob_house(arr, start, end):
    memo = [0] * (len(arr) + 1)
    memo[0] = 0
    memo[1] = arr[0]

    for idx in range(1, len(memo) - 1):
        memo[idx + 1] = max(memo[idx], arr[idx] + memo[idx - 1])
    
    return memo[-1]

def house_robber_ii(nums):
    assert 1 <= len(nums) <= 100
    assert all(0 <= nums[i] <= 100 for i in range(len(nums)))

    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])

    #Passed indices because slicing takes O(n) space in Python3
    return max(rob_house(nums, 0, len(nums) - 1), rob_house(nums, 1, len(nums)))

# Tests...
"""
Input                   Expected            Actual
 0  1  2
[2, 3, 2]                3                   3
 
rob_house(nums, 0, 2)
idx = 0
t1 = 2
t2 = 3
ans = 3

rob_house(nums, 1, 3)
idx = 1
t1 = 3
t2 = 2
ans = 3

---------------------------
 0 1 2 3 4
[1,3,1,3,100]           103             101         {FAILED TESTCASE} -> Core logic wrong -> We can skip multiple houses in between
 ^
rob_house(nums, 0, 4)
idx = 2 (0, 2)
t1 = 2
t2 = 6
ans = 6

rob_house(nums, 1, 5)
idx = 3 (1, 3)
t1 = 3 + 3 = 6
t2 = 101
ans = 101

max(6, 101) = 101
"""

# Debugging...
"""
The problem is same as House Robber
rob_house => Reference: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
 0  1  2  3  4
[1, 3, 1, 3, 100]
            Two choices => Add 0                        Don't add 0
                                 ans = 0,[1, 3, 1, 3, 100]
                    1 [1, 3, 100]                   0, [3, 1, 3, 100]
            2 [100]      1, [3, 100]        3,[3, 100]              0, [1, 3, 100]

        ...         ...         ...         ...         ...         ...         ...


Bottom-up => 
 0  1  2  3  4
[1, 3, 1, 3, 100]
memo = 
[0, 1]

memo[i+1] = Math.max(memo[i], memo[i-1] + val);
"""