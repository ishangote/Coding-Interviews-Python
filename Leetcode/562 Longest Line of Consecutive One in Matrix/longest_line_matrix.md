# 562. Longest Line of Consecutive One in Matrix

## Problem Statement

> Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
> The line could be horizontal, vertical, diagonal, or anti-diagonal.

> Constraints:
>
> - m == mat.length
> - n == mat[i].length
> - 1 <= m, n <= 10<sup>4</sup>
> - 1 <= m \* n <= 10<sup>4</sup>
> - mat[i][j] is either 0 or 1.

## Examples

Example 1:

```
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
```

Example 2:

```
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
```

## Depth First Search With Memoization Solution

```
Input:

mat =
        0.  1.  2.  3.
    0.  0   0   0   1*  For each direction compute the max length
    1.  0   1   1*  0
    2.  0   1*  1   0
    3.  1*  0   0   1


mat =
        0.  1.  2.  3.
    0.  0   0   0   1
    1.  0   1   1*  0   Memoize the (row, col, direction) to avoid recomputation of max length for the vector starting at row, col in direction
              /
    2.  0   1*  1   0
          /
    3.  1*  0   0   1

```
