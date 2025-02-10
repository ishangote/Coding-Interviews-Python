# 84. Largest Rectangle in Histogram

## Problem Statement

> Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

> Constraints:
>
> - 1 <= heights.length <= 10<sup>5</sup>
> - 0 <= heights[i] <= 10<sup>4</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
Input: heights = [2,4]
Output: 4
```

## Brute Force Solution

```
Approach 1:
Brute Force: height of the rectangle formed between any two bars will always be limited by the height of the shortest bar lying between them
For two pointers, calculate min height bar between them and calculate area

Time Complexity: O(n^3)
Space Complexity: O(1)

Approach 2:
Better Brute Force: height of the rectangle formed between any two bars will always be limited by the height of the shortest bar lying between them
For two pointers, we can find the bar of minimum height for current pair by using the minimum height bar of the previous pair.

Time Complexity: O(n^2)
Space Complexity: O(1)
```

## Monotonic Stack Solution

```
Input:
           0  1  2  3  4  5  6
heights = [2, 1, 5, 3, 6, 2, 3]

            6
        5   -
        -   -
        - 3 -   3
    2   - - - 2 -
    - 1 - - - - -
    - - - - - - -
    0 1 2 3 4 5 6
      *   ^   *
    <----   ---->
prev             next
smaller          smaller
index            index

Intuition: Rectangle with height 3 at index 3 is bound by [prev smaller, next smaller]

Problem          |  Traversal Direction  |   Stack
-------------------------------------------------------
Next Greater     |  Left to Right        |   Decreasing
Previous Greater |  Right to Left        |   Decreasing
Next Smaller     |  Left to Right        |   Increasing *
Previous Smaller |  Right to Left        |   Increasing *

Output:
```
