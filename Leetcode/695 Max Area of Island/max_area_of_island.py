import unittest


def recursive_helper(row, col, visited, area, grid):
    area[0] += 1
    visited.add((row, col))
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row_dir, col_dir in DIRECTIONS:
        next_row, next_col = row + row_dir, col + col_dir

        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] == 1
            and (next_row, next_col) not in visited
        ):
            recursive_helper(next_row, next_col, visited, area, grid)


# Time: O(m * n), where m => number of rows, n => number of cols
# Space: O(m * n)
def max_area_of_island(grid):
    res = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                area = [0]
                recursive_helper(row, col, visited, area, grid)
                res = max(res, area[0])
    return res


class TestMaxAreaOfIsland(unittest.TestCase):
    def test_max_area_of_island(self):
        self.assertEqual(
            max_area_of_island(
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ]
            ),
            6,
        )
        self.assertEqual(max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]), 0)


if __name__ == "__main__":
    unittest.main()
