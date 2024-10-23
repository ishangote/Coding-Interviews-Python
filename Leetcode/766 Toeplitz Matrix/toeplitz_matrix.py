import unittest


# Time: O(n x m), where n => number of rows in matrix and m => number of cols in matrix
# Space: O(1)
def toeplitz_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            next_row = row + 1
            next_col = col + 1

            if (
                next_row >= len(matrix)
                or next_col >= len(matrix[0])
                or matrix[row][col] == matrix[next_row][next_col]
            ):
                continue

            return False

    return True


class TestToeplitzMatrix(unittest.TestCase):
    def test_toeplitz_matrix(self):
        self.assertTrue(toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
        self.assertFalse(toeplitz_matrix([[1, 2], [2, 2]]))


if __name__ == "__main__":
    unittest.main()
