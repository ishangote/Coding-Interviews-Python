# 56. Merge Intervals

## Problem Statement

> Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

> Constraints:
>
> - 1 <= intervals.length <= 10<sup>4</sup>
> - intervals[i].length == 2
> - 0 <= starti <= endi <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

Example 2:

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Sorting + Stack Solution

```
Input:
intervals =
[[1, 3], [2, 6], [8, 10], [15, 18]]

Initialize
sort intervals
stack = [[1, 3]]

   0.      1.       2.       3.
[[1, 3], [2, 6], [8, 10], [15, 18]]
           ^
Initialize
stack = [[1, 3]]            * if overlap with top of stack, then pop, merge and put

Output:
[[1, 6], [8, 10], [15, 18]]

```
