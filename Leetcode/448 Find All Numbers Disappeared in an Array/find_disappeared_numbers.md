# 448. Find All Numbers Disappeared in an Array

## Problem Statement

> Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
>
> Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

> Constraints:
>
> - n == nums.length
> - 1 <= n <= 10<sup>5</sup>
> - 1 <= nums[i] <= n

## Examples

Example 1:

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

Example 2:

```
Input: nums = [1,1]
Output: [2]
```

## Brute Force Solution

```
nums = [4, 3, 2, 7, 8, 2, 3, 1]

nums_set = { 4, 3, 2, 7, 8, 1 }

n = 8 => {1, 2, 3, 4, 5, 6, 7, 8} are possible missing candidates

* for each candidate, check if it is nums

* Time: O(n)
* Space: O(n)
```

## Optimized Solution

```
* how would a complete nums look?
            0  1  2  3  4  5  6  7
complete = [1, 2, 3, 4, 5, 6, 7, 8]

* Notice, we can identify numbers by their indices as well since 1 <= nums[i] <= n

        0  1  2   3  4  5  6  7
nums = [4, 3, 2, -7, 8, 2, 3, 1]         * 4's ideal position will be at idx = 3, hence we mark nums[idx] as negative
        ^

        0  1   2   3  4  5  6  7
nums = [4, 3, -2, -7, 8, 2, 3, 1]
           ^

        0   1   2   3  4  5  6  7
nums = [4, -3, -2, -7, 8, 2, 3, 1]       * while checking num at each idx as we iterate, we must take abs(nums[idx]) since it can be marked as negative
                ^

        0   1   2   3  4  5   6  7
nums = [4, -3, -2, -7, 8, 2, -3, 1]
                    ^

        0   1   2   3  4  5   6   7
nums = [4, -3, -2, -7, 8, 2, -3, -1]
                       ^

        0   1   2   3  4  5   6   7
nums = [4, -3, -2, -7, 8, 2, -3, -1]
                          ^

        0   1   2   3  4  5   6   7
nums = [4, -3, -2, -7, 8, 2, -3, -1]
                              ^

         0   1   2   3  4  5   6   7
nums = [-4, -3, -2, -7, 8, 2, -3, -1]
                                   ^

         0   1   2   3  4  5   6   7
nums = [-4, -3, -2, -7, 8, 2, -3, -1]

* Notice that the indices with positive numbers must indicate the missing numbers.
* At idx 4, we are expecting number 5 and at idx 5 we are expecting number 6

* Time: O(n), where n => length of nums
* Space: O(1)
```
