# 739. Daily Temperatures

## Problem Statement

> Given an array of integers `temperatures` represents the daily temperatures, return an array answer such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

> Constraints:
>
> - 1 <= temperatures.length <= 10<sup>5</sup>
> - 30 <= temperatures[i] <= 100

## Examples

Example 1:

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

Example 2:

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

Example 3:

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Monotonic Stack Solution

```
Problem          |  Traversal Direction  |   Stack
-------------------------------------------------------
Next Greater     |  Left to Right        |   Decreasing     *
Previous Greater |  Right to Left        |   Decreasing
Next Smaller     |  Left to Right        |   Increasing
Previous Smaller |  Right to Left        |   Increasing


Input:
temperatures =
 0   1   2   3   4   5   6   7
[73, 74, 75, 71, 69, 72, 76, 73]
     ^

stack = [0]
         ^
         pop -> update result at index 0 = (1 - 0)

       0  1  2  3  4  5  6  7
res = [1, 0, 0, 0, 0, 0, 0, 0]


temperatures =
 0   1   2   3   4   5   6   7
[73, 74, 75, 71, 69, 72, 76, 73]
         ^

stack = [1]
         ^
         pop -> update result at index 1 = (2 - 1)

       0  1  2  3  4  5  6  7
res = [1, 1, 0, 0, 0, 0, 0, 0]


temperatures =
 0   1   2   3   4   5   6   7
[73, 74, 75, 71, 69, 72, 76, 73]
                     ^

stack = [2, 3, 4]
               ^
               pop -> update result at index 4 (5 - 4)

stack = [2, 3]
            ^
            pop -> update result at index 3 (5 - 3)

       0  1  2  3  4  5  6  7
res = [1, 1, 0, 2, 1, 0, 0, 0]

...

Output:
[1, 1, 4, 2, 1, 1, 0, 0]
```
