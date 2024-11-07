# 1428. Leftmost Column with at Least a One

## Problem Statement

> A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

> Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.
>
> You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
>
> - `BinaryMatrix.get(row, col)` returns the element of the matrix at index (row, col) (0-indexed).
> - `BinaryMatrix.dimensions()` returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
>
> Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
>
> For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-5.jpg)

```
Input: mat = [[0,0],[1,1]]
Output: 0
```

Example 2:
![Example 2](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-4.jpg)

```
Input: mat = [[0,0],[0,1]]
Output: 1
```

Example 3:
![Example 3](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-3.jpg)

```
Input: mat = [[0,0],[0,0]]
Output: -1
```

## Brute Force Solution

```
rows = n
cols = m

* iterate over each column
    * iterate over each row
        * if matrix[row][col] == 1: return col
```

## Binary Search Solution

```
* matrix is row sorted => non-decreasing rows

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0* (if last element of row is zero => entire row is zero)
  1.  0   0   1   1   1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1


      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0   1   1   1* (if last element of row is 1, find first 1 (binary search))
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1

Time: O(n * logm)
```

## Exploratory Search Solution

```
Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0* (if last element of row is zero, we move down a row)
  1.  0   0   1   1   1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0   1   1   1* (the res can be to the left, move left)
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0*  1   1   1     * move down till we find 1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0   1   1   1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1*  1   1   1

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0   1   1   1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0*  1   1   1   1

Input:
      0.  1.  2.  3.  4.
  0.  0   0   0   0   0
  1.  0   0   1   1   1
  2.  0   0   0   0   1
  3.  0   0   0   0   0
  4.  0   1   1   1   1
  5.  *                     => res = col + 1 (res must be to the right)


* When we encounter a 0, we know that the leftmost 1 can't be to the left of it.
* When we encounter a 1, we should continue the search on that row (move pointer to the left), in order to find an even smaller index.
* At each step, we're moving 1 step left or 1 step down. Therefore, we'll always finish looking at either one of the M rows or N columns.
* Therefore, we'll stay in the grid for at most N+M steps, and therefore get a time complexity of O(N+M).
```

## Approach Summary

1. Brute Force:

- For each column, iterate through all rows to find the first '1'.
- Time: O(n \* m) (not optimal).

2. Binary Search on Rows (Optimized):

- Idea: Since each row is sorted, use binary search to find the first '1' in each row.
- If the last element in a row is 0, skip to the next row.
- Time Complexity: O(n \* log m)

3. Exploration Approach (Most Optimal):

- Idea: Start at the top-right corner. Move left on encountering '1' (try to minimize column index) or move down on '0' (row doesn't have an earlier '1').
- Time Complexity: O(n + m)
