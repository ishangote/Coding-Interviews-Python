import unittest


def recursive_helper(row, col, grid):
    if row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == 1:
        return 0

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1

    return recursive_helper(row + 1, col, grid) + recursive_helper(row, col + 1, grid)


# Time: O(2^(m+n)), where m => number of rows, n => number of cols
# Space: O(m + n), (Implied Call Stack Memory)
def unique_paths_ii_recursive(grid):
    return recursive_helper(0, 0, grid)


# --------------------------------------------------------------------- #


def recursive_helper_memo(row, col, memo, grid):
    if row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == 1:
        return 0

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1

    if (row, col) in memo:
        return memo[(row, col)]

    memo[(row, col)] = recursive_helper_memo(
        row + 1, col, memo, grid
    ) + recursive_helper_memo(row, col + 1, memo, grid)

    return memo[(row, col)]


# Time: O(m*n), where m => number of rows, n => number of cols
# Space: O(m*n) => Dominated by memo. Recursion Call Stack is still O(m + n)
def unique_paths_ii_recursive_memo(grid):
    return recursive_helper_memo(0, 0, {}, grid)


# --------------------------------------------------------------------- #


class TestUniquePathsII(unittest.TestCase):
    def test_unique_paths_ii_recursive(self):
        self.assertEqual(
            unique_paths_ii_recursive([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2
        )

    def test_unique_paths_ii_recursive_memo(self):
        self.assertEqual(
            unique_paths_ii_recursive_memo([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2
        )


if __name__ == "__main__":
    unittest.main()
