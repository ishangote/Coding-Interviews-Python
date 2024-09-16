# 45 Jump Game II

## Problem Statement

> You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
>
> Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
>
> - 0 <= j <= nums[i]
> - i + j < n
>
> Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

## BFS Solution

Calculate the number of levels/zones in the array. Iterate in the zone to figure out the indices of the next zone.

```
Example 1:

nums =
 0  1  2  3  4
[2, 3, 1, 1, 4]
 ^
    *  *
   jumps = 1

 0  1  2  3  4
[2, 3, 1, 1, 4]
    ^
          *  *
          jumps = 2


nums=
 0  1  2  3  4
[3, 1, 3, 1, 4]
 _
 ^
    l
          r


nums=
 0  1  2  3  4  5
[3, 1, 3, 1, 4]
    _______
       ^
             l
                r

right >= len(nums) - 1 => stop

```

## References

- Leetcode: https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
- Youtube: https://www.youtube.com/watch?v=dJ7sWiOoK7g
