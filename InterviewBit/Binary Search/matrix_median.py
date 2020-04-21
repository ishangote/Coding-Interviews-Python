"""
Given a matrix of integers A of size N x M in which each row is sorted.
Find an return the overall median of the matrix A.
Note: No extra memory is allowed.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Return the overall median of the matrix A.

Constraints
1 <= N, M <= 10^5
1 <= N*M  <= 10^6
1 <= A[i] <= 10^9
N*M is odd

Each row is sorted =>

A:
  0  1  2
0 1, 3, 7
1 2, 7, 9
2 3, 6, 9

3x3 matrix

Sorted Array ->
0  1  2  3  4  5  6  7  8
1, 2, 3, 3, 6, 7, 7, 9, 9
lb                      ub

median_pos = (3 * 3 + 1) // 2 = 5

mid = lb + ub // 2 = 5

"""
from bisect import bisect_right
# Binary Search Solution
def matrix_median(matrix):
    if not matrix: return None
    lb, ub = float('inf'), -float('inf')

    for i in range(len(matrix)):
        lb = min(lb, matrix[i][0])
        ub = max(ub, matrix[i][len(matrix[0]) - 1])

    median_pos = (len(matrix) * len(matrix[0]) + 1) // 2

    while lb < ub:
        mid = (lb + ub) // 2
        loc = [0]
        # bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
        # bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.
        for i in range(len(matrix)):
            j = bisect_right(matrix[i], mid)
            loc[0] = loc[0] + j

        if loc[0] < median_pos: lb = mid + 1
        else: ub = mid

    return lb

import unittest
class TestMatrixMedian(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(matrix_median([[1, 3, 5], [2, 6, 9], [3, 6, 9]]), 5)

if __name__ == "__main__":unittest.main()