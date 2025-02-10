# 33. Search in Rotated Sorted Array

## Problem Statement

> There is an integer array `nums` sorted in ascending order (with distinct values).
>
> Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` `(1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` `(0-indexed)`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.
>
> Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
>
> You must write an algorithm with O(log n) runtime complexity.

> Constraints:
>
> 1 <= nums.length <= 5000
> -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
> All values of nums are unique.
> nums is an ascending array that is possibly rotated.
> -10<sup>4</sup> <= target <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

Example 3:

```
Input: nums = [1], target = 0
Output: -1
```

## Binary Search Solution

```
Input:
target = 6
nums =
 0  1  2  3  4  5  6
[4, 5, 6, 7, 0, 1, 2]


## Search Pivot: Binary Search ##
[4  5   6   7   0   1   2]
                *
              pivot -> nums[pivot - 1] > nums[pivot]

 0  1  2  3  4  5  6
[4, 5, 6, 7, 0, 1, 2]
 l        m        h        -> nums[mid] > nums[hi]

 0  1  2  3  4
[4, 0, 1, 2, 3]
 l     m     h              -> nums[mid] < nums[hi]

Pseudo:
if nums[mid - 1] > nums[mid]: return mid
if nums[mid] >  nums[hi]:
    lo = mid + 1
else nums[mid] < nums[hi]:
    hi = mid - 1

Edge Case:
[1, 2, 3, 4]
 l  m
 h      * STOP l == h => return l


## Search Target: Binary Search ##

pivot = 4
 0  1  2  3  4  5  6
[4, 5, 6, 7, 0, 1, 2]
 ----------  -------

pivot = 1
 0  1  2  3  4
[4, 0, 1, 2, 3]
 -  ----------

Pseudo:
if nums[pivot] <= target <= nums[-1]: search [pivot, len(nums))
else: search [0, pivot)

Output: 2
```
