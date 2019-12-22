# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""
    0  1  2

0   1, 2, 3
1   4, 5, 6
2   7, 8, 9

result = []
fr, lr = 0, 2
fc, lc = 0, 2

    0  1  2

0   
1   4, 5
2   7, 8

result = [1,2,3, 6,9]
fr, lr = 1, 2
fc, lc = 0, 1

    0  1  2

0   
1   5
2   

result = [1,2,3, 6,9, 8,7,4, ]
fr, lr = 1, 1
fc, lc = 0, 0

    0  1  2

0   
1   
2   

result = [1,2,3, 6,9, 8,7,4, 5]
fr, lr = 1, 0 -> break
fc, lc = 0, 0

return [1,2,3, 6,9, 8,7,4, 5]

"""

def spiral_matrix(matrix):
    result = []

    last_row = len(matrix) - 1
    last_col = len(matrix[0]) - 1

    first_row, first_col = 0, 0

    while first_row <= last_row and first_col <= last_col:
        for idx in range(first_col, last_col + 1):
            result.append(matrix[first_row][idx])

        first_row += 1

        for idx in range(first_row, last_row + 1):
            result.append(matrix[idx][last_col])

        last_col -= 1

        if first_row <= last_row:
            for idx in range(last_col, first_col - 1, -1):
                result.append(matrix[last_row][idx])
        
        last_row -= 1

        if first_col <= last_col:
            for idx in range(last_row, first_row - 1, -1):
                result.append(matrix[idx][first_col])
            
        first_col += 1
    
    return result

#-------------------------------------------------

import unittest
class TestSpiralMatrixPrint(unittest.TestCase):
    def test_one_row_matrix(self):
        self.assertEqual(spiral_matrix([[1, 2, 3, 4]]), [1, 2, 3, 4])
    
    def test_one_column_matrix(self):
        self.assertEqual(spiral_matrix([[1], [2], [3], [4]]), [1, 2, 3, 4])

    def test_empty_matrix(self):
        self.assertEqual(spiral_matrix([[], []]), [])

    def test_spiral_matrix(self):
        self.assertEqual(spiral_matrix([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])

if __name__ =="__main__": unittest.main()