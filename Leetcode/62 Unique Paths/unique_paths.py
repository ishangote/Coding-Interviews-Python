import unittest


def recursive_helper(row, col, memo, target_row, target_col):
    if row > target_row or col > target_col:
        return 0
    if row == target_row and col == target_col:
        return 1
    if (row, col) in memo:
        return memo[(row, col)]

    memo[(row, col)] = recursive_helper(
        row + 1, col, memo, target_row, target_col
    ) + recursive_helper(row, col + 1, memo, target_row, target_col)

    return memo[(row, col)]


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(m*n)
def unique_paths_recursive(rows, cols):
    return recursive_helper(0, 0, {}, rows - 1, cols - 1)


# --------------------------------------------------------------------- #


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(n*n)
def unique_paths_dp(rows, cols):
    memo = [[0] * cols for _ in range(rows)]

    for col in range(cols):
        memo[0][col] = 1

    for row in range(rows):
        memo[row][0] = 1

    for row in range(1, rows):
        for col in range(1, cols):
            memo[row][col] = memo[row - 1][col] + memo[row][col - 1]

    return memo[-1][-1]


# --------------------------------------------------------------------- #


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(n)
def unique_paths_dp_optimized(rows, cols):
    prev_row = [1] * cols

    for _ in range(1, rows):
        cur_row = [1] + [0] * (cols - 1)

        for col in range(1, cols):
            cur_row[col] = prev_row[col] + cur_row[col - 1]

        prev_row = cur_row

    return prev_row[-1]


# --------------------------------------------------------------------- #


def recursive_helper(row, col, cur_path, paths, target_row, target_col):
    if row > target_row or col > target_col:
        return 0
    if row == target_row and col == target_col:
        paths.append(cur_path)
        return

    recursive_helper(row + 1, col, cur_path + "D", paths, target_row, target_col)
    recursive_helper(row, col + 1, cur_path + "R", paths, target_row, target_col)


# Return ALL paths from (0, 0) to (m - 1, n - 1)
# Time: O(2^(m+n)), where m => number of rows, n => number of cols
# Space: O(m+n), in the worst case, need to make m−1 down moves and n−1 right moves before reaching the target.
def unique_paths_variation(rows, cols):
    paths = []
    recursive_helper(0, 0, "", paths, rows - 1, cols - 1)
    return paths


# --------------------------------------------------------------------- #


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths_recursive(self):
        self.assertEqual(unique_paths_recursive(3, 4), 10)
        self.assertEqual(unique_paths_recursive(3, 1), 1)

    def test_unique_paths_dp(self):
        self.assertEqual(unique_paths_dp(3, 4), 10)
        self.assertEqual(unique_paths_dp(3, 1), 1)

    def test_unique_paths_dp_optimized(self):
        self.assertEqual(unique_paths_dp_optimized(3, 4), 10)
        self.assertEqual(unique_paths_dp_optimized(3, 1), 1)

    def test_unique_paths_variation(self):
        self.assertListEqual(
            unique_paths_variation(3, 4),
            [
                "DDRRR",
                "DRDRR",
                "DRRDR",
                "DRRRD",
                "RDDRR",
                "RDRDR",
                "RDRRD",
                "RRDDR",
                "RRDRD",
                "RRRDD",
            ],
        )
        self.assertListEqual(unique_paths_variation(3, 1), ["DD"])


if __name__ == "__main__":
    unittest.main()
