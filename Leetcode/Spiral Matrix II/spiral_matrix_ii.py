"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

def spiral_matrix_ii(n):
    if n < 1: return []
    matrix = [[0 for i in range(n)] for j in range(n)]
    
    count = 1

    last_row = len(matrix) - 1
    last_col = len(matrix[0]) - 1

    first_row, first_col = 0, 0

    while first_row <= last_row and first_col <= last_col:
        for idx in range(first_col, last_col + 1):
            # result.append(matrix[first_row][idx])
            matrix[first_row][idx] = count
            count += 1

        first_row += 1

        for idx in range(first_row, last_row + 1):
            # result.append(matrix[idx][last_col])
            matrix[idx][last_col] = count
            count += 1 

        last_col -= 1

        if first_row <= last_row:
            for idx in range(last_col, first_col - 1, -1):
                # result.append(matrix[last_row][idx])
                matrix[last_row][idx] = count
                count += 1
        
        last_row -= 1

        if first_col <= last_col:
            for idx in range(last_row, first_row - 1, -1):
                # result.append(matrix[idx][first_col])
                matrix[idx][first_col] = count
                count += 1
                
        first_col += 1

    return matrix

import unittest
class TestSpiralMatrixII(unittest.TestCase):
    def test_edge_case(self):
        self.assertEqual(spiral_matrix_ii(-3), [])
        self.assertEqual(spiral_matrix_ii(0), [])
        self.assertEqual(spiral_matrix_ii(1), [[1]])

    def test_generic(self):
        self.assertEqual(spiral_matrix_ii(3), [[1,2,3],[8,9,4],[7,6,5]])

if __name__ == "__main__": unittest.main()