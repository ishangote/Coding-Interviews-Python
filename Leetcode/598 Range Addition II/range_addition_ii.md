# 598. Range Addition II

## Problem Statement

> You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
>
> Count and return the number of maximum integers in the matrix after performing all the operations.

> Constraints:
>
> - 1 <= m, n <= 4 \* 10<sup>4</sup>
> - 0 <= ops.length <= 10<sup>4</sup>
> - ops[i].length == 2
> - 1 <= ai <= m
> - 1 <= bi <= n

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg)

```
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
```

Example 2:

```

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
```

Example 3:

```
Input: m = 3, n = 3, ops = []
Output: 9
```

## Brute Force Solution

```
Input:
matrix =
            0   0   0
            0   0   0
            0   0   0

operations = [[2, 2], [3, 3]]
                 ^

matrix =
            0.  1.  2.
        0.  0   0   0
        1.  0   0   0
        2.  0   0   0

* increment all numbers in range 0 -> 2 row and 0 -> 2 col

            0.  1.  2.
        0.  1   1   0
        1.  1   1   0
        2.  0   0   0


operations = [[2, 2], [3, 3]]
                         ^

matrix =
            0.  1.  2.
        0.  0   0   0
        1.  0   0   0
        2.  0   0   0

* increment all numbers in range 0 -> 3 row and 0 -> 3 col

            0.  1.  2.
        0.  2   2   1
        1.  2   2   1
        2.  1   1   1

* Keep track of the max number while incrementing numbers

* Count maximum numbers

            0.  1.  2.
        0.  2   2   1
        1.  2   2   1
        2.  1   1   1

Output: 4
```

## Optimization

![Optimization](https://leetcode.com/problems/range-addition-ii/Figures/598_Range_Addition2.PNG)

```
Input:
m = 6, n = 5

matrix =
            0.  1.  2.  3.  4.
        0.  0   0   0   0   0
        1.  0   0   0   0   0
        2.  0   0   0   0   0
        3.  0   0   0   0   0
        4.  0   0   0   0   0
        5.  0   0   0   0   0

operations = [[2, 2], [3, 3]]



matrix =
            0.  1.  2.  3.  4.
        0.  1   1   0   0   0
        1.  1   1   0   0   0
        2.  0   0   0   0   0
        3.  0   0   0   0   0
        4.  0   0   0   0   0
        5.  0   0   0   0   0

operations = [[2, 2], [3, 3]]
                 ^


matrix =
            0.  1.  2.  3.  4.
            -----
        0. |2   2|  1   0   0
        1. |2   2|  1   0   0
            -----
        2.  1   1   1   0   0
        3.  0   0   0   0   0
        4.  0   0   0   0   0
        5.  0   0   0   0   0

operations = [[2, 2], [3, 3]]
                         ^

* The maximum number will always be at location (0, 0)
* We need the size of 2 2 matrix
                      2 2

* The top left location is (0, 0) and
* bottom right location is (2, 2) (non inclusive) i.e min (operations[row]), min(operations[col])

* The actual maximum number will be length of operations, since (0, 0) will be updated for every operation
```
