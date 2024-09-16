import unittest


# Time: O(n^2) where n is number of rows
# Space: O(1)
def pascals_triangle(rows):
    res = [[1]]

    for itr in range(1, rows):
        current_row = []
        previous_row = res[itr - 1]

        for idx in range(len(previous_row) + 1):
            left_top = (
                0 if not 0 <= idx - 1 < len(previous_row) else previous_row[idx - 1]
            )

            right_top = 0 if not 0 <= idx < len(previous_row) else previous_row[idx]

            current_row.append(left_top + right_top)

        res.append(current_row)

    return res


class TestPascalsTriangle(unittest.TestCase):
    def test_pascals_triangle(self):
        self.assertEqual(pascals_triangle(1), [[1]])
        self.assertEqual(pascals_triangle(2), [[1], [1, 1]])
        self.assertEqual(pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(pascals_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(
            pascals_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )


if __name__ == "__main__":
    unittest.main()
