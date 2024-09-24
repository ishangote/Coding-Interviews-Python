# 252. Meeting Rooms

## Problem Statement

> Given an array of meeting time intervals where intervals[i] = [start<sub>i</sub>, end<sub>i</sub>], determine if a person could attend all meetings.

> Constraints:
>
> - 0 <= intervals.length <= 104
> - intervals[i].length == 2
> - 0 <= starti < endi <= 106

## Examples

Example 1:

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

Example 2:

```
Input: intervals = [[7,10],[2,4]]
Output: true
```

## Sort Intervals Solution

```
Input:
intervals =
[[7, 10], [2, 4]]

* sort intervals based on start

[[2, 4], [7, 10]]
    ^       *

* end(idx) >= start(idx + 1)

Output: True
```
