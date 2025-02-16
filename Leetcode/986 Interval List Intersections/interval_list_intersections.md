# 986. Interval List Intersections

## Problem Statement

> You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise disjoint and in sorted order.
> Return the intersection of these two interval lists.
> A closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.
> The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

> Constraints:
>
> - 0 <= firstList.length, secondList.length <= 1000
> - firstList.length + secondList.length >= 1
> - 0 <= starti < endi <= 10<sup>9</sup>
> - endi < starti+1
> - 0 <= startj < endj <= 10<sup>9</sup>
> - endj < startj+1

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

Example 2:

```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

## Two Pointers Solution

```
Two Lists Overlap IF:
- start of one interval < end of the other
- this condition needs to be true for both intervals
- s1 < e2 and s2 < e1
- overlapping part = [max(s1, s2), min(e1, e2)]
- if e1 <= e2 => move pt1
- else => move pt2

Input:

first_list =  [[0, 3], [5, 7]]
                         ^
second_list = [[2, 6]]
                 *

-------------      ------------
        *****************           ********

0   1   2   3   4   5   6   7   8   9   10   11     12

Output:
[[2, 3], [5, 6]]
```

## Mistakes in Thinking - Interval Intersection Problem

1. Incorrectly Handling Non-Overlapping Intervals:
   I incremented both pointers (pt1 and pt2) when intervals didn’t overlap, which skipped potential intersections.
   **Instead, I should only advance the pointer for the interval that ends first to correctly check the next overlap.**
