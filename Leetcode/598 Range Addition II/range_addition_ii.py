import unittest


# Time: O(o * m * n), where o => number of operations
# Space: O(m * n)
def range_addition_ii_brute_force(m, n, operations):
    if not operations:
        return m * n

    matrix = [[0 for col in range(n)] for row in range(n)]
    max_num = 0

    for op in operations:
        [rows, cols] = op

        for r in range(rows):
            for c in range(cols):
                matrix[r][c] += 1
                max_num = max(max_num, matrix[r][c])

    res = 0
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == max_num:
                res += 1

    return res


# Time: O(o) where o => number of operations
# Space: O(1)
def range_addition_ii_optimized(m, n, operations):
    bottom_right_row, bottom_right_col = m, n

    for op in operations:
        bottom_right_row = min(bottom_right_row, op[0])
        bottom_right_col = min(bottom_right_col, op[1])

    return bottom_right_row * bottom_right_col


class TestRangeAdditionII(unittest.TestCase):
    def test_range_addition_ii_brute_force(self):
        self.assertEqual(range_addition_ii_brute_force(3, 3, []), 9)
        self.assertEqual(range_addition_ii_brute_force(3, 3, [[2, 2], [3, 3]]), 4)
        self.assertEqual(
            range_addition_ii_brute_force(
                3,
                3,
                [
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                ],
            ),
            4,
        )

    def test_range_addition_ii_optimized(self):
        self.assertEqual(range_addition_ii_optimized(3, 3, []), 9)
        self.assertEqual(range_addition_ii_optimized(3, 3, [[2, 2], [3, 3]]), 4)
        self.assertEqual(
            range_addition_ii_optimized(
                3,
                3,
                [
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                ],
            ),
            4,
        )


if __name__ == "__main__":
    unittest.main()
