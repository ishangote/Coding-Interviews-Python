"""
Solutions: https://www.youtube.com/watch?v=FOa55B9Ikfg

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Approach: REDUCTION IN SEARCH SPACE!
Operations:
To go to greater values: right, down
To go to lower values: left, up

Where to start? 
left-up corner -> no operations to go to lower values
right-bottom corner -> no operations to go to greater values
left-bottom corner -> all ops valid
right-up corner -> all ops valid

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

left-bottom corner -> all ops valid -> let's start at this point

"""
#O(n + m)
def search_2d_matrix_2(matrix, target):
    if not matrix: return False
    # left-bottom corner -> all ops valid -> let's start at this point
    row = len(matrix) - 1
    col = 0

    while col < len(matrix[0]) and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else: return True
    
    return False

import unittest
class TestSearch2DMatrix2(unittest.TestCase):
    def test_generic(self):
        matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        self.assertEqual(search_2d_matrix_2(matrix, 14), True)
        self.assertEqual(search_2d_matrix_2(matrix, 121), False)

if __name__ == "__main__": unittest.main()