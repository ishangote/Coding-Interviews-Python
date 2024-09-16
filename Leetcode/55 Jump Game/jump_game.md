# 55 Jump Game

## Problem Statement

> You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

> Constraints:
> 1 <= nums.length <= 104
> 0 <= nums[i] <= 105

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

## Brute Force

```
Build decision tree
From idx = 0 we can move to idx = 1, 2, 3
From idx = 3 we can not move

        *
        0  1  2  3  4
nums = [3, 2, 1, 0, 4]
           ^  ^  ^

              idx=0
        1         2        3
    2      3      3
    3

Time complexity: O(n^n)

Memoization: memo[idx] = True/False -> Reduce time complexity to O(n^2)
```

## Greedy Solution

```
We can reach the destination if we are at destination. Move destination backwards.

Example 1:

nums=
 0  1  2  3  4
[2, 3, 1, 1, 4]
             ^ (goal)
          * (itr)

 0  1  2  3  4
[2, 3, 1, 1, 4]
          ^
       *

 0  1  2  3  4
[2, 3, 1, 1, 4]
       ^
    *

 0  1  2  3  4
[2, 3, 1, 1, 4]
    ^
 *

 0  1  2  3  4
[2, 3, 1, 1, 4]
 ^ (goal = 0)
*

Example 2:

nums =
 0  1  2  3  4
[3, 2, 1, 0, 4]
             ^ (goal)
          * (itr)

 0  1  2  3  4
[3, 2, 1, 0, 4]
             ^
       *

 0  1  2  3  4
[3, 2, 1, 0, 4]
             ^
    *

 0  1  2  3  4
[3, 2, 1, 0, 4]
             ^
 *

 0  1  2  3  4
[3, 2, 1, 0, 4]
             ^ (goal = 4)
*

Time Complexity: O(n)
Space Complexity: O(1)
```

## References:

- Leetcode: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
- Youtube: https://www.youtube.com/watch?v=Yan0cv2cLy8
