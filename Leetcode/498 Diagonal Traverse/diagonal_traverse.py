import unittest


# Time: O(n * m), where n => number of rows, m => number of cols
# Space: O(1)
def diagonal_traverse(matrix):
    res = []

    if not matrix or not matrix[0]:
        return res

    row, col = 0, 0
    direction = "UP"

    while len(res) < len(matrix) * len(matrix[0]):
        res.append(matrix[row][col])

        if direction == "UP":
            if col == len(matrix[0]) - 1:
                row += 1
                direction = "DOWN"

            elif row == 0:
                col += 1
                direction = "DOWN"

            else:
                row, col = row - 1, col + 1

        elif direction == "DOWN":
            if row == len(matrix) - 1:
                col += 1
                direction = "UP"

            elif col == 0:
                row += 1
                direction = "UP"

            else:
                row, col = row + 1, col - 1

        else:
            pass

    return res


class TestDiagonalTraverse(unittest.TestCase):
    def test_diagonal_traverse(self):
        self.assertEqual(
            diagonal_traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 4, 7, 5, 3, 6, 8, 9],
        )
        self.assertEqual(diagonal_traverse([[1, 2], [3, 4]]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
