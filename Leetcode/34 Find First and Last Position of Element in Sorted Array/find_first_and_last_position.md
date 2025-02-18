# 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

> Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
>
> If target is not found in the array, return `[-1, -1]`.
>
> You must write an algorithm with `O(log n)` runtime complexity.

> Constraints:
>
> - 0 <= nums.length <= 10<sup>5</sup>
> - -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
> - nums is a non-decreasing array.
> - -10<sup>9</sup> <= target <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

Example 3:

```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Binary Search Solution

```
Input:
target = 8

Binary Search to find lower bound =>
nums =
 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
 l     m        h           l = mid + 1

 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
          l  m  h           h = mid

 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
          l  h              h = mid
          m

 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
          l                 while l < h
          h

Binary Search to find higher bound =>

 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
          l  m                  l = m  + 1
                h

 0  1  2  3  4  5
[5, 7, 7, 8, 8, 10]
                l               h = mid - 1
             h  m
Output:

```
