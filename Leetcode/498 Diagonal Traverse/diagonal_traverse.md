# 498. Diagonal Traverse

## Problem Statement

> Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

> Constraints:
>
> - m == mat.length
> - n == mat[i].length
> - 1 <= m, n <= 10<sup>4</sup>
> - 1 <= m \* n <= 10<sup>4</sup>
> - -10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

Example 2:

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

## Solution

```
Input:
m =
           0   1   2  <- cols
           ----------
      0 |  1   2   3
      1 |  6   7   8
      2 |  2   3   4

* Simulation
1. Move to the Up-Right until you can't move
2. Move one step to the Right, if you can’t move to the Right, move one step Down
3. Move to the Down-Left until you can't move
4. Move one step Down, if you can’t move, move one step to the Right

r   c   val
0   0   1
0   1   2
1   0   6
2   0   2
1   1   7
0   2   3
1   2   8
2   1   3
2   2   4
```
