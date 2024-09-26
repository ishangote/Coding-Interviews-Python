# 346. Moving Average from Data Stream

## Problem Statement

> Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
>
> Implement the MovingAverage class:
>
> - MovingAverage(int size) Initializes the object with the size of the window size.
> - double next(int val) Returns the moving average of the last size values of the stream.

> - Constraints:
> -
> - 1 <= size <= 1000
> - -10<sup>5</sup> <= val <= 10<sup>5</sup>
> - At most 10<sup>4</sup> calls will be made to next.

## Examples

Example 1:

```
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

## Solution

```
k = 3
nums  = []

1  -> nums = [1] -> average = 1
10 -> nums = [1, 10] -> average = 1 + 10 // 2 = 5.5
3  -> nums = [1, 10, 3] -> average = 1 + 10 + 3 // 3 = 4.6

             0   1  2  3
5 -> nums = [1, 10, 3, 5]   -> average = 10 + 3 + 5 // 3 = 6
                --------

* maintain the total sum of the window.
* when window shifts, subtract the number from total sum

```
