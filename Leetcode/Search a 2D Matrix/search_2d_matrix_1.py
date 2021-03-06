"""
Solutions: https://www.youtube.com/watch?v=FOa55B9Ikfg

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
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

# ------------------------------------------ #

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

# ------------------------------------------ #

def get_row(matrix, target):
    # Two Binary Search O(logn) + O(logm)
    lo, hi = 0, len(matrix) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
            return mid
        if matrix[mid][0] > target: hi = mid - 1
        else: lo = mid + 1
    return -1

def binary_search(matrix, row, target):
    lo, hi = 0, len(matrix[0]) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[row][mid] == target: return True
        if matrix[row][mid] < target: lo = mid + 1
        else: hi = mid - 1
    return False

def search_2d_matrix_optimized(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0 or target is None: return False
    row = get_row(matrix, target)
    return binary_search(matrix, row, target)

import unittest
class TestSearch2DMatrix1(unittest.TestCase):
    def test_genric(self):
        matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
        self.assertEqual(search_2d_matrix_approach1(matrix, 3), True)
        self.assertEqual(search_2d_matrix_approach1(matrix, 13), False)

        self.assertEqual(search_2d_matrix(matrix, 3), True)
        self.assertEqual(search_2d_matrix(matrix, 13), False)

        self.assertEqual(search_2d_matrix_optimized(matrix, 3), True)
        self.assertEqual(search_2d_matrix_optimized(matrix, 13), False)
        self.assertEqual(search_2d_matrix_optimized([[1]], 2), False)
        self.assertEqual(search_2d_matrix_optimized([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0), True)

        
if __name__ == "__main__": unittest.main()