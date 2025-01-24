import unittest
import sys


# Time: O(r*c*c), where r => number of rows and c => number of cols
# Space: O(1)
def maximum_number_of_points(matrix):
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):

            max_points = -sys.maxsize
            for prev_col in range(len(matrix[0])):
                max_points = max(
                    max_points,
                    matrix[row][col] + matrix[row - 1][prev_col] - abs(col - prev_col),
                )

            matrix[row][col] = max_points

    return max(matrix[-1])


# Time: O(r*c), where r => number of rows, c => number of columns
# Space: O(c)
def maximum_number_of_points_optimized(matrix):
    rows, cols = len(matrix), len(matrix[0])
    memo = matrix[0]

    for row in range(1, rows):
        left_max = [memo[0] + 0] * cols
        right_max = [memo[-1] - (cols - 1)] * cols

        for col in range(1, cols):
            left_max[col] = max(left_max[col - 1], memo[col] + col)

        for col in range(cols - 2, -1, -1):
            right_max[col] = max(right_max[col + 1], memo[col] - col)

        next_memo = [0] * cols
        for col in range(cols):
            next_memo[col] = matrix[row][col] + max(
                left_max[col] - col, right_max[col] + col
            )

        memo = next_memo

    return max(memo)


class TestMaximumNumberOfPoints(unittest.TestCase):
    def test_max_number_of_points(self):
        self.assertEqual(maximum_number_of_points([[1, 2, 3], [1, 5, 1], [3, 1, 1]]), 9)
        self.assertEqual(maximum_number_of_points([[1, 5], [2, 3], [4, 2]]), 11)

    def test_max_number_of_points_optimized(self):
        self.assertEqual(
            maximum_number_of_points_optimized([[1, 2, 3], [1, 5, 1], [3, 1, 1]]), 9
        )
        self.assertEqual(
            maximum_number_of_points_optimized([[1, 5], [2, 3], [4, 2]]), 11
        )


if __name__ == "__main__":
    unittest.main()
