import unittest
import sys


def recursive_helper(grid, row, col, area, island_label):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area[0] += 1
    grid[row][col] = island_label
    for row_dir, col_dir in DIRECTIONS:
        next_row, next_col = row + row_dir, col + col_dir

        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] == 1
        ):
            recursive_helper(grid, next_row, next_col, area, island_label)


def compute_island_areas(grid):
    island_area = {}
    island_label = 2

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 1:
                continue
            area = [0]
            recursive_helper(grid, row, col, area, island_label)
            island_area[island_label] = area[0]
            island_label += 1

    return island_area


def calculate_potential_island(row, col, island_area, grid):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area = 1
    visited = set()
    for row_dir, col_dir in DIRECTIONS:
        next_row, next_col = row + row_dir, col + col_dir

        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] in island_area
            and grid[next_row][next_col] not in visited
        ):
            area += island_area[grid[next_row][next_col]]
            visited.add(grid[next_row][next_col])

    return area


# Time: O(m * n), where m => number of rows
# Space: O(m * n)
def making_a_large_island(grid):
    island_area = compute_island_areas(grid)
    res = -sys.maxsize

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                continue
            res = max(res, calculate_potential_island(row, col, island_area, grid))

    return max(res, max(island_area.values(), default=0))


class TestMakingALargeIsland(unittest.TestCase):
    def test_making_a_large_island(self):
        grid1 = [[1, 0], [0, 1]]
        self.assertEqual(making_a_large_island(grid1), 3)

        grid2 = [[1, 1], [1, 0]]
        self.assertEqual(making_a_large_island(grid2), 4)

        grid3 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.assertEqual(making_a_large_island(grid3), 9)

        grid4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(making_a_large_island(grid4), 1)

        grid5 = [[1, 1], [1, 1]]
        self.assertEqual(making_a_large_island(grid5), 4)


if __name__ == "__main__":
    unittest.main()
