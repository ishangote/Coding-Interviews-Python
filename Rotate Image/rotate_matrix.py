# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
"""
Approach 1:
    0   1   2
 0  1   2   3
 1  4   5   6
 2  7   8   9

Transpose:

    0   1   2 
 0  1   4   7
 1  2   5   8
 2  3   6   9
 
Rev all rows ->
 
     0   1   2
 0   7   4   1
 1   8   5   2
 2   9   6   3

"""

def rotate_matrix(matrix):
    if not matrix or len(matrix) != len(matrix[0]): return None

    #Transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    
    return matrix

import unittest
class TestRotateMatrix(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(rotate_matrix([]), None)
        self.assertEqual(rotate_matrix([[1, 2, 3], [4, 5, 6]]), None)

    def test_rotate_matrix_generic(self):
        self.assertEqual(rotate_matrix([[1,2,3], [4,5,6], [7,8,9]]), [[7,4,1], [8,5,2], [9,6,3]])
        self.assertEqual(rotate_matrix([[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]), [[15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11]])

if __name__ == "__main__": unittest.main()