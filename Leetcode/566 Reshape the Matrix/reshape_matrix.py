import unittest


# Time: O(n x m), where n => number of rows in mat and m => number of cols in mat
# Space: O(1), excluding the result
def reshape_matrix(mat, row, col):
    if row * col != len(mat) * len(mat[0]):
        return mat

    res = [[-1 for c in range(col)] for r in range(row)]
    cur_row, cur_col = 0, 0

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            res[cur_row][cur_col] = mat[r][c]

            cur_col += 1
            if cur_col == col:
                cur_col = 0
                cur_row += 1

    return res


class TestReshapeMatrix(unittest.TestCase):
    def test_reshape_matrix(self):
        self.assertEqual(reshape_matrix([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])
        self.assertEqual(reshape_matrix([[1, 2], [3, 4]], 4, 1), [[1], [2], [3], [4]])


if __name__ == "__main__":
    unittest.main()
