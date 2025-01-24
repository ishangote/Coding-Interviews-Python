# 539. Minimum Time Difference

## Problem Statement

> Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
>
> Constraints:
>
> - 2 <= timePoints.length <= 2 \* 10<sup>4</sup>
> - timePoints[i] is in the format "HH:MM".

## Examples

Example 1:

```
Input: timePoints = ["23:59","00:00"]
Output: 1
```

Example 2:

```
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
```

## Solution

```
Input:
times =
["17:30", "14:30", "00:00", "01:00", "23:59"]


hours           minutes
0               0
1               1
2               2
3               3
...             ...
23              59


time_in_mins =
[17*60 + 30, 14 * 60 + 30, 0 * 60 + 0, 1 * 60 + 0, 23 * 60 + 59]

[1050, 870, 0, 60, 1439]

sort => [0, 60, 870, 1050, 1439]
                 ^
                     *
        (min = 60)

* EDGE CASE: an edge case we have to consider is if the smallest difference is between the last and first element, in which case the time loops back to "00:00".
* For example, if the last and first time is "22:00" and "02:00", then the time difference is 4 hours or 240 minutes.

* 00:00 is same as 24:00 => 24 * 60 + 0 = 1440

* example if we had 02:00 as first element and 22:00 as last element => [120, 1320]
* check 1440 + 120 - 1320 = 240
* Append 1440 + times[0] to the end of the list

=>
[0, 60, 870, 1050, 1439, 1440 + 0]
                    ^
                           *
                   (min = 1)

Output:
1
```
