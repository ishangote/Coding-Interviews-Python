# 35. Search Insert Position

## Problem Statement

> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
> You must write an algorithm with O(log n) runtime complexity.

> Constraints:
>
> - 1 <= nums.length <= 104
> - -104 <= nums[i] <= 104
> - nums contains distinct values sorted in ascending order.
> - -104 <= target <= 104

## Examples

Example 1

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

Example 2

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

Example 3

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Binary Search

```
* Note: nums contains DISTINCT values

Example 1:

target = 4
nums =
 0  1  2  3
[1, 3, 5, 6]
 l
          h

mid = 3 + 0 // 2 = 1
target > mid => move to right

nums =
 0  1  2  3
[1, 3, 5, 6]
       l
          h

mid = 3 + 2 // 2 = 2
target < mid => move to left

nums =
 0  1  2  3
[1, 3, 5, 6]
       l
       h

return l

Output: 2

```
