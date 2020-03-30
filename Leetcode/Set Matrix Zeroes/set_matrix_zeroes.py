"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


1 4 0 2
6 3 9 8
1 0 2 1
2 1 2 0

does first row have zero? = True
does first col have zero? = False

------------------------------------

1 4 0 2
1 3 9 8
1 0 2 1
2 1 2 0

Iterate from second row, second column i.e index [1, 1]
Mark [i][0]  = [0][j] if 0

1     4 0 2     1     0 0 2
      *               *
1     3 9 8  => 1     3 9 8
1    *0 2 1     0    *0 2 1
2     1 2 0     2     1 2 0


1     0 0 2     1     0 0 0
          *               *
1     3 9 8  => 1     3 9 8
0     0 2 1     0     0 2 1
2     1 2 0*    0     1 2 0*

------------------------------------

1 4 0 2     0 0 0 0
6 3 9 8     6 0 0 0
1 0 2 1  => 1 0 0 0
2 1 2 0     0 0 0 0

"""
def set_matrix_zero(matrix):
    #The all() method returns True when all elements in the given iterable are true. If not, it returns False.

    if not matrix or not matrix[0]: return

    first_row_zero_flag = not all(matrix[0])
    first_col_zero_flag = False

    for row in matrix:
        if row[0] == 0: 
          first_col_zero_flag = True
          break
    
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[0][col] = matrix[row][0] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    if first_row_zero_flag:
        matrix[0] = [0] * len(matrix[0])

    if first_col_zero_flag:
        for row in matrix:
            row[0] = 0

    return matrix

import unittest
class TestSetMatrixZeroes(unittest.TestCase):
    def test_generic(self):
      self.assertEqual(set_matrix_zero([[1],[0]]), [[0],[0]])
      self.assertEqual(set_matrix_zero([[1,1,1], [1,0,1], [1,1,1]]), [[1,0,1], [0,0,0], [1,0,1]])
      self.assertEqual(set_matrix_zero([[0,1,2,0], [3,4,5,2], [1,3,1,5]]), [[0,0,0,0], [0,4,5,0], [0,3,1,0]])

if __name__ == "__main__": unittest.main()