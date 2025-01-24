import unittest
import sys


# Time: O(r*c), where r => number of rows, c => number of cols
# Space: O(1)
def minimum_falling_path_sum(matrix):
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):

            left_diagonal = (
                matrix[row - 1][col - 1]
                if 0 <= col - 1 < len(matrix[0])
                else sys.maxsize
            )

            up = matrix[row - 1][col]

            right_diagonal = (
                matrix[row - 1][col + 1]
                if 0 <= col + 1 < len(matrix[0])
                else sys.maxsize
            )

            matrix[row][col] += min(left_diagonal, up, right_diagonal)

    return min(matrix[-1])


class TestMinimumFallingPathSum(unittest.TestCase):
    def test_minimum_falling_path_sum(self):
        self.assertEqual(
            minimum_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13
        )
        self.assertEqual(minimum_falling_path_sum([[-19, 57], [-40, -5]]), -59)


if __name__ == "__main__":
    unittest.main()
