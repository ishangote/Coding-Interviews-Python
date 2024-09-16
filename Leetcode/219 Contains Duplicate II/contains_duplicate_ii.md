# 219. Contains Duplicate II

## Problem Statement

> Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

> Constraints:
>
> - 1 <= nums.length <= 105
> - -109 <= nums[i] <= 109
> - 0 <= k <= 105

## Examples

Example 1:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Example 2:

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

Example 3:

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Brute Force

```
Input:
k = 3
nums =
 0  1  2  3
[1, 2, 3, 1]
 i        j

abs(i - j) = 3 <= k

Output: true

* The size of the window must be k + 1. (4 numbers)

Algorithm:
1. Iterate over the array, for each index check in previous k indices
```

## Sliding Window Optimization

```
Example 1:

k = 2
nums =
 0  1  2  3  4  5
[1, 2, 3, 1, 3, 1]
 ^
 *

window = {1}

nums =
 0  1  2  3  4  5
[1, 2, 3, 1, 3, 1]
 ^
    *

window = {1, 2}


nums =
 0  1  2  3  4  5
[1, 2, 3, 1, 3, 1]
 ^
    ^
       *

window = {1, 2, 3} => {2, 3} => size = k + 1 => remove num at ^


nums =
 0  1  2  3  4  5
[1, 2, 3, 1, 3, 1]
    ^
       ^
          *

window = {2, 3, 1} => {3, 1}


nums =
 0  1  2  3  4  5
[1, 2, 3, 1, 3, 1]
       ^
             * => already part of window => return true

window = {3, 1} => {3, 1}
```

## References

1. [Leetcode](https://leetcode.com/problems/contains-duplicate-ii/)
2. [Youtube](https://www.youtube.com/watch?v=ypn0aZ0nrL4&ab_channel=NeetCodeIO)
