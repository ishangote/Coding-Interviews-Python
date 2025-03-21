import unittest


def recursive_helper(row, col, target_row, target_col):
    if row > target_row or col > target_col:
        return 0
    if row == target_row and col == target_col:
        return 1

    return recursive_helper(row + 1, col, target_row, target_col) + recursive_helper(
        row, col + 1, target_row, target_col
    )


# Time: O(2^(m+n)), where m => number of rows, n => number of cols
# Space: O(m + n), (Implied Call Stack Memory)
def unique_paths_recursive(rows, cols):
    return recursive_helper(0, 0, rows - 1, cols - 1)


# --------------------------------------------------------------------- #


def recursive_helper_memo(row, col, memo, target_row, target_col):
    if row > target_row or col > target_col:
        return 0
    if row == target_row and col == target_col:
        return 1
    if (row, col) in memo:
        return memo[(row, col)]

    memo[(row, col)] = recursive_helper_memo(
        row + 1, col, memo, target_row, target_col
    ) + recursive_helper_memo(row, col + 1, memo, target_row, target_col)

    return memo[(row, col)]


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(m*n) => Dominated by memo. Recursion Call Stack is still O(m + n)
def unique_paths_recursive_memo(rows, cols):
    return recursive_helper_memo(0, 0, {}, rows - 1, cols - 1)


# --------------------------------------------------------------------- #


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(m*n) => dominated by the memo table
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

## * VARIATION: Return ALL paths from (0, 0) to (m - 1, n - 1) ##


def recursive_helper_paths_variation(row, col, cur_path, paths, target_row, target_col):
    if row > target_row or col > target_col:
        return
    if row == target_row and col == target_col:
        paths.append(cur_path)
        return

    recursive_helper_paths_variation(
        row + 1, col, cur_path + "D", paths, target_row, target_col
    )
    recursive_helper_paths_variation(
        row, col + 1, cur_path + "R", paths, target_row, target_col
    )


# Time: O(2^(m+n)), where m => number of rows, n => number of cols
# Space: O(m+n), in the worst case, need to make m−1 down moves and n−1 right moves before reaching the target.
def unique_paths_paths_variation(rows, cols):
    paths = []
    recursive_helper_paths_variation(0, 0, "", paths, rows - 1, cols - 1)
    return paths


# --------------------------------------------------------------------- #


def recursive_helper_paths_variation_memo(row, col, target_row, target_col, memo):
    # If out of bounds, there are no paths.
    if row > target_row or col > target_col:
        return []
    # If the destination is reached, return a list with an empty path.
    if row == target_row and col == target_col:
        return [""]
    # Return memoized result if available.
    if (row, col) in memo:
        return memo[(row, col)]

    paths = []
    # Get all paths by moving down.
    for path in recursive_helper_paths_variation_memo(
        row + 1, col, target_row, target_col, memo
    ):
        paths.append("D" + path)
    # Get all paths by moving right.
    for path in recursive_helper_paths_variation_memo(
        row, col + 1, target_row, target_col, memo
    ):
        paths.append("R" + path)

    # Cache the computed paths for this cell.
    memo[(row, col)] = paths
    return paths


# Time Complexity:
#   O(2^(m+n)) in the worst case (with m = target_row + 1 and n = target_col + 1), since the number of valid paths is exponential.
#   Memoization avoids redundant calculations but cannot reduce the number of paths generated.
#
# Space Complexity:
#   O(m+n) for the recursion stack and O(2^(m+n)) for storing all valid paths.
def unique_paths_paths_variation_memo(rows, cols):
    memo = {}
    return recursive_helper_paths_variation_memo(0, 0, rows - 1, cols - 1, memo)


# --------------------------------------------------------------------- #


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths_recursive(self):
        self.assertEqual(unique_paths_recursive(3, 4), 10)
        self.assertEqual(unique_paths_recursive(3, 1), 1)

    def test_unique_paths_recursive_memo(self):
        self.assertEqual(unique_paths_recursive_memo(3, 4), 10)
        self.assertEqual(unique_paths_recursive_memo(3, 1), 1)

    def test_unique_paths_dp(self):
        self.assertEqual(unique_paths_dp(3, 4), 10)
        self.assertEqual(unique_paths_dp(3, 1), 1)

    def test_unique_paths_dp_optimized(self):
        self.assertEqual(unique_paths_dp_optimized(3, 4), 10)
        self.assertEqual(unique_paths_dp_optimized(3, 1), 1)

    def test_unique_paths_variation(self):
        self.assertListEqual(
            unique_paths_paths_variation(3, 4),
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
        self.assertListEqual(unique_paths_paths_variation(3, 1), ["DD"])

    def test_unique_paths_paths_variation_memo(self):
        self.assertListEqual(
            unique_paths_paths_variation_memo(3, 4),
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
        self.assertListEqual(unique_paths_paths_variation_memo(3, 1), ["DD"])


if __name__ == "__main__":
    unittest.main()
