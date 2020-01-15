"""
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.
Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A = 
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
"""
def search_2d_matrix_approach1(matrix, target):
    #O(n^2)
    if not matrix or not matrix[0]: return False
    for i in range(len(matrix)):
        if target==matrix[i][-1]: return True
        elif target<matrix[i][-1]:
            for j in range(len(matrix[0])):
                if matrix[i][j]==target: return True
            return False
    return False

def search_2d_matrix(matrix, target):
    #Binary Search Approach O(ln(m*n))
    if not matrix or target is None: return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        #Very imp: row = mid // cols, col = mid % cols
        num = matrix[mid // cols][mid % cols]

        if num == target: return True
        elif num < target: left = mid + 1
        else: right = mid - 1

    return False

import unittest
class TestSearch2DMatrix1(unittest.TestCase):
    def test_genric(self):
        matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
        self.assertEqual(search_2d_matrix_approach1(matrix, 3), True)
        self.assertEqual(search_2d_matrix_approach1(matrix, 13), False)

if __name__ == "__main__": unittest.main()