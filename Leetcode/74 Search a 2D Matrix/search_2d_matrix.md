# 74. Search a 2D Matrix

## Problem Statement

> You are given an m x n integer matrix matrix with the following two properties:
>
> - Each row is sorted in non-decreasing order.
> - The first integer of each row is greater than the last integer of the previous row.
>
> Given an integer target, return true if target is in matrix or false otherwise.
>
> You must write a solution in O(log(m \* n)) time complexity.

> Constraints:
>
> - m == matrix.length
> - n == matrix[i].length
> - 1 <= m, n <= 100
> - -10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## Binary Search Solution

```
Input:
matrix =

    0.  1.  2.  3.
0.  1   3   5   7
1.  10  11  16  20
2.  23  30  34  60

target = 11

- Binary Search to target row
setup: lo, hi = (0, rows)
condition:
    mid_row[-1] == target or mid_row[0] <= target <= mid_row[-1]:
        target row => mid_row
    mid_row[-1] < target: lo = mid + 1
    mid_row[-1] > target: hi = mid

- Binary Search to search target in target row

target = 4
 0  1  2  3  4
[3, 4, 4, 6, 7]
 l     m     h

target = 5
 0  1  2  3  4
[3, 4, 6, 6, 7]
 l     m     h

 0  1  2  3  4
[3, 4, 6, 6, 7]
 l  m  h

 0  1  2  3  4
[3, 4, 6, 6, 7]
       l
       h
       m

 0  1  2  3  4
[3, 4, 6, 6, 7]
       l
    h
```

## References

- https://www.youtube.com/watch?v=FOa55B9Ikfg
