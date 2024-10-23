# 766. Toeplitz Matrix

## Problem Statement

> Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
> A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

> Constraints:
>
> - m == matrix.length
> - n == matrix[i].length
> - 1 <= m, n <= 20
> - 0 <= matrix[i][j] <= 99

> Follow up:
>
> - What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
> - What if the matrix is so large that you can only load up a partial row into the memory at once?

## Examples

Example 1:

```
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

Example 2:

```
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
```

## Solution

```
matrix =
     0  1  2  3  -> cols
  0  1  2  3  4
  1  5  1  2  3
  2  9  5  1  2

* Pseudo Code:

for r in range[0, 4):
    for c in range[0, 3):
        next_r = r + 1
        next_c = c + 1

        mat[r][c] != mat[next_r][next_c]: return False

return True
```

## Follow-up 1

```
In order to handle the follow-up, we need to rely on the fact that the next element in a diagonal is on the next row in the next column.
We can keep a Deque/LinkedList tracking what value is expected in each row (expected_row).
Evaluate the matrix row by row removing the rightmost element in the deque and adding the current row's first element to the left of the deque.
You can then compare every cell in your expected_row to the current row. The indices will line up.
Initially, the expected row just contains the values from the first row in the matrix.
```

## Follow-up 2

```
For the follow-up 2, we can only load a partial row at one time. We could split the whole matrix vertically into several sub-matrices, while each sub-matrix should have one column overlapped. We repeat the same method in follow-up 1 for each sub-matrix.

For example:

[1 2 3 4 5 6 7 8 9 0]              [1 2 3 4]              [4 5 6 7]              [7 8 9 0]
[0 1 2 3 4 5 6 7 8 9]              [0 1 2 3]              [3 4 5 6]              [6 7 8 9]
[1 0 1 2 3 4 5 6 7 8]     -->      [1 0 1 2]       +      [2 3 4 5]       +      [5 6 7 8]
[2 1 0 1 2 3 4 5 6 7]              [2 1 0 1]              [1 2 3 4]              [4 5 6 7]
[3 2 1 0 1 2 3 4 5 6]              [3 2 1 0]              [0 1 2 3]              [3 4 5 6]
```

## References

1. [Analysis of follow-up questions](https://leetcode.com/problems/toeplitz-matrix/solutions/271388/Java-Solution-for-Follow-Up-1-and-2/)
