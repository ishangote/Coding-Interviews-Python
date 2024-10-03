# 485. Max Consecutive Ones

## Problem Statement

> Given a binary array nums, return the maximum number of consecutive 1's in the array.

> Constraints:
>
> - 1 <= nums.length <= 10<sup>5</sup>
> - nums[i] is either 0 or 1.

## Examples

Example 1:

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

Example 2:

```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

## Solution

```
Input:
nums = [1, 1, 0, 1, 1, 1]
max_count = -inf
count = 0


nums = [1, 1, 0, 1, 1, 1]
        ^
max_count = 1
count = 1


nums = [1, 1, 0, 1, 1, 1]
           ^
max_count = 2
count = 2


nums = [1, 1, 0, 1, 1, 1]
              ^
max_count = 2           * since array has only 1's and 0's we can simply reset count
count = 0


nums = [1, 1, 0, 1, 1, 1]
                 ^
max_count = 2
count = 1


nums = [1, 1, 0, 1, 1, 1]
                    ^
max_count = 2
count = 2


nums = [1, 1, 0, 1, 1, 1]
                       ^
max_count = 3
count = 3


Output:
3
```
