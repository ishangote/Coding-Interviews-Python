# 419. Battleships in a Board

## Problem Statement

> Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
>
> Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2024/06/21/image.png)

```
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
```

Example 2:

```
Input: board = [["."]]
Output: 0
```

## Depth-First Search Solution

```
Input:
board =

    0 1 2 3 4 5
0   X . . . . X
1   . . X X . X
2   . . . . . .
3   X X X . . .

* Traverse the board. If cell contains X, increment result and mark the entire battleship with '.'
```
