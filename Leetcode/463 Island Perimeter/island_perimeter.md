# 463. Island Perimeter

## Problem Statement

> You are given row x col grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.
>
> Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
>
> The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
>
> Determine the perimeter of the island.

> Constraints:
>
> - row == grid.length
> - col == grid[i].length
> - 1 <= row, col <= 100
> - grid[i][j] is 0 or 1.
> - There is exactly one island in grid.

## Examples

Example 1:

![alt text](https://assets.leetcode.com/uploads/2018/10/12/island.png)

```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

Example 2:

```
Input: grid = [[1]]
Output: 4
```

Example 3:

```
Input: grid = [[1,0]]
Output: 4
```

## Solution

```
Input:
grid =
          0  1  2  3 <- cols
       0  0  1  0  0
       1  1  1  1  0
       2  0  1  0  0
       3  1  1  0  0
       ^
    rows

res = 0

-----------------------------------

grid =
          0  1   2  3 <- cols
       0  0  1*  0  0
       1  1  1   1  0
       2  0  1   0  0
       3  1  1   0  0
       ^
    rows

pos = [0, 1]
res = 3 (since 3 sides have 0 and 1 (bottom has island))

-----------------------------------

grid =
          0   1  2  3 <- cols
       0  0   1  0  0
       1  1*  1  1  0
       2  0   1  0  0
       3  1   1  0  0
       ^
    rows

pos = [1, 0]
res = 3 + 3 = 6

-----------------------------------

grid =
          0  1   2  3 <- cols
       0  0  1   0  0
       1  1  1*  1  0
       2  0  1   0  0
       3  1  1   0  0
       ^
    rows

pos = [1, 1]
res = 6 + 0 = 6

-----------------------------------

grid =
          0  1  2   3 <- cols
       0  0  1  0   0
       1  1  1  1*  0
       2  0  1  0   0
       3  1  1  0   0
       ^
    rows

pos = [1, 2]
res = 6 + 3 = 9

-----------------------------------

grid =
          0  1   2  3 <- cols
       0  0  1   0  0
       1  1  1   1  0
       2  0  1*  0  0
       3  1  1   0  0
       ^
    rows

pos = [2, 1]
res = 9 + 2 = 11

-----------------------------------

grid =
          0   1  2  3 <- cols
       0  0   1  0  0
       1  1   1  1  0
       2  0   1  0  0
       3  1*  1  0  0
       ^
    rows

pos = [3, 0]
res = 11 + 3 = 14

-----------------------------------

grid =
          0  1   2  3 <- cols
       0  0  1   0  0
       1  1  1   1  0
       2  0  1   0  0
       3  1  1*  0  0
       ^
    rows

pos = [3, 1]
res = 14 + 2 = 16

Output:
16
```
