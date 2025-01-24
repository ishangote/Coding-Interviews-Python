# 1937. Maximum Number of Points with Cost

## Problem Statement

> You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
>
> To gain points, you must pick one cell in each row. Picking the cell at coordinates `(r, c)` will add `points[r][c]` to your score.
>
> However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows `r` and `r + 1` `(where 0 <= r < m - 1)`, picking cells at coordinates `(r, c1) and (r + 1, c2)` will subtract `abs(c1 - c2)` from your score.
>
> Return the maximum number of points you can achieve.

> Constraints:
>
> - m == points.length
> - n == points[r].length
> - 1 <= m, n <= 10<sup>5</sup>
> - 1 <= m \* n <= 10<sup>5</sup>
> - 0 <= points[r][c] <= 10<sup>5</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png)

```
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png)

```
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
```

## Dynamic Programming Solution

```
Input:
matrix =
[
    [1, 2, 3],
    [1*, 5, 1],  <- max(1 + 1 - 0, 1 + 2 - 1, 1 + 3 - 2)
    [3, 1, 1]
]

[
    [1, 2, 3],
    [2, 5*, 1], <-  max(5 + 1 - 1, 5 + 2 - 0, 5 + 3 - 1)
    [3, 1, 1]
]

[
    [1, 2, 3],
    [2, 7, 1*], <- max(1 + 1 - 2, 1 + 2 - 1, 1 + 3 - 0)
    [3, 1, 1]
]

[
    [1, 2, 3],
    [2, 7, 4],
    [3*, 1, 1]  <- max(3 + 2 - 0, 3 + 7 - 1, 3 + 4 - 2)
]

[
    [1, 2, 3],
    [2, 7, 4],
    [9, 1*, 1]  <- max(1 + 2 - 1, 1 + 7 - 0, 1 + 4 - 1)
]

[
    [1, 2, 3],
    [2, 7, 4],
    [9, 8, 1*]  <- max(1 + 2 - 2, 1 + 7 - 1, 1 + 4 - 0)
]


[
    [1, 2, 3],
    [2, 7, 4],
    [9, 8, 7]   <- return max(9, 8, 7) -> 9
]

Output: 9
```

## Dynamic Programming Optimized Solution

```
DP Formula =>
matrix[i][j] = matrix[i][j] + matrix[i - 1][k] - abs(j - k)

k => iteration over columns in previous row


Case 1: j > k: abs(j - k) = j - k

matrix[i][j] = matrix[i][j] + matrix[i - 1][k] - j + k
             = (matrix[i - 1][k] + k) + (matrix[i][j] - j)
             = matrix[i][j] + (matrix[i - 1][k] + k) - j
                              <-------------------->
                              left_max: prefix sum from left to right (j > k)

Case 2: j < k: abs(j - k) = k - j

matrix[i][j] = matrix[i][j] + matrix[i - 1][k] - k + j
             = (matrix[i - 1][k] - k) + (matrix[i][j] + j)
             = matrix[i][j] + (matrix[i - 1][k] - k) + j
                              <-------------------->
                              right_max: prefix sum from right to left (j < k)

=> Max score is max(case1, case2)
```
