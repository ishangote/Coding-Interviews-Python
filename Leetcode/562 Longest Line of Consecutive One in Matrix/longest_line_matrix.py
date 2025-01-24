import unittest


def recursive_helper(matrix, memo, row, col, offset):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col]:
        if (row, col, offset) not in memo:
            memo[(row, col, offset)] = 1 + recursive_helper(
                matrix, memo, row + offset[0], col + offset[1], offset
            )

        return memo[(row, col, offset)]

    return 0


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(m*n)
def longest_line_matrix(matrix):
    res = 0
    memo = {}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                for offset in directions:
                    res = max(res, recursive_helper(matrix, memo, row, col, offset))

    return res


class TestLongestLineMatrix(unittest.TestCase):
    def test_longest_line_matrix(self):
        matrix = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(longest_line_matrix(matrix), 3)

        matrix = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(longest_line_matrix(matrix), 4)

        matrix = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
        self.assertEqual(longest_line_matrix(matrix), 4)


if __name__ == "__main__":
    unittest.main()
