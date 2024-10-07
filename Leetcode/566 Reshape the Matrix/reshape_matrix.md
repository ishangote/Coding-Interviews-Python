# 566. Reshape the Matrix

## Problem Statement

> In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
>
> You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
>
> The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
>
> If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

> Constraints:
>
> - m == mat.length
> - n == mat[i].length
> - 1 <= m, n <= 100
> - -1000 <= mat[i][j] <= 1000
> - 1 <= r, c <= 300

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
```

## Solution

```
Input:
mat =
    [
        [1   2]
        [3   4]
    ]

r = 1
c = 4


    [
        [1*  2]
        [3   4]
    ]

cur_row = 0
cur_col = 0
res = [[1, -1, -1, -1]]
        ^

    [
        [1   2*]
        [3   4]
    ]

cur_row = 0
cur_col = 1
res = [[1, 2, -1, -1]]
           ^

    [
        [1   2]
        [3*  4]
    ]

cur_row = 0
cur_col = 2
res = [[1, 2, 3, -1]]
              ^

    [
        [1   2]
        [3   4*]
    ]

cur_row = 0
cur_col = 3
res = [[1, 2, 3, 4]]
                 ^

Output: [[1 2 3 4]]
```

```
Input:
mat =
    [
        [1   2]
        [3   4]
    ]

r = 4
c = 1

cur_row, cur_col = 0, 0

res = [[-1],
       [-1],
       [-1],
       [-1]]


    [
        [1*   2]
        [3   4]
    ]

cur_row = 0
cur_col = 0

res = [[1], <
       [-1],
       [-1],
       [-1]]


    [
        [1   2*]
        [3   4]
    ]

cur_row = 1
cur_col = 0

res = [[1],
       [2], <
       [-1],
       [-1]]

...

Output: [[1],
         [2],
         [3],
         [4]]
```
