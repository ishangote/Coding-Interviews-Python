import unittest
import sys


class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, row, col):
        return self.matrix[row][col]

    def dimensions(self):
        return [len(self.matrix), len(self.matrix[0])]


# ---------------------------------------------------- #


def search_column_with_one(matrix, row, cols):
    if matrix.get(row, cols - 1) == 0:
        return sys.maxsize

    lo, hi = 0, cols - 1

    while lo < hi:
        mid = (lo + hi) // 2
        mid_value = matrix.get(row, mid)

        if mid_value == 0:
            lo = mid + 1

        else:
            hi = mid

    return lo


# Time: O(nlogm), where n => number of rows, m => number of cols
# Space: O(1)
def left_most_column_with_one_binary_search(matrix: BinaryMatrix) -> int:
    rows, cols = matrix.dimensions()
    res = sys.maxsize

    for row in range(rows):
        res = min(res, search_column_with_one(matrix, row, cols))

    return -1 if res == sys.maxsize else res


# ---------------------------------------------------- #


# Time: O(n + m), where n => number of rows, m => number of cols
# Space: O(1)
def left_most_column_with_one_exploration(matrix: BinaryMatrix) -> int:
    rows, cols = matrix.dimensions()

    cur_row, cur_col = 0, cols - 1

    while cur_row < rows and cur_col >= 0:
        value = matrix.get(cur_row, cur_col)

        if value == 0:
            cur_row += 1
        else:
            cur_col -= 1

    return cur_col + 1 if cur_col != cols - 1 else -1


# ---------------------------------------------------- #


class TestLeftMostColumnWithOne(unittest.TestCase):
    def test_left_most_column_binary_search(self):
        matrix1 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1],
            ]
        )

        self.assertEqual(left_most_column_with_one_binary_search(matrix1), 1)

        matrix2 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
            ]
        )

        self.assertEqual(left_most_column_with_one_binary_search(matrix2), 2)

        matrix3 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )

        self.assertEqual(left_most_column_with_one_binary_search(matrix3), -1)

    def test_left_most_column_exploration(self):
        matrix1 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1],
            ]
        )

        self.assertEqual(left_most_column_with_one_exploration(matrix1), 1)

        matrix2 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
            ]
        )

        self.assertEqual(left_most_column_with_one_exploration(matrix2), 2)

        matrix3 = BinaryMatrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )

        self.assertEqual(left_most_column_with_one_binary_search(matrix3), -1)


if __name__ == "__main__":
    unittest.main()
