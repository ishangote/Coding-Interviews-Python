# 931. Minimum Falling Path Sum

## Problem Statement

> Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
>
> A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

> Constraints:
>
> - n == matrix.length == matrix[i].length
> - 1 <= n <= 100
> - -100 <= matrix[i][j] <= 100

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

## Dynamic Programming Solution

```

Input:

   0.  1.  2.
0. 2   1   3
1. 6   5*  4    * At point 5 we can have path => 2 + 5 OR 1 + 5 OR 3 + 5 (minimize it)
2. 7   8   9

Dynamic Programming Formula:
mat[i][j] = mat[i][j] + min(mat[i - 1][j - 1], mat[i - 1][j], mat[i - 1][j + 1])

Output:
13
```
