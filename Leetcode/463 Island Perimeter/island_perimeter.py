import unittest


def is_water_at_pos(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return 1 if grid[row][col] == 0 else 0
    return 1


def perimeter_at_pos(grid, row, col):
    return (
        is_water_at_pos(grid, row - 1, col)
        + is_water_at_pos(grid, row + 1, col)
        + is_water_at_pos(grid, row, col - 1)
        + is_water_at_pos(grid, row, col + 1)
    )


# Time: O(r x c), where r => number of rows, c => number of cols
# Space: O(1)
def island_perimeter(grid):
    res = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue

            res += perimeter_at_pos(grid, row, col)

    return res


import unittest


class TestIslandPerimeter(unittest.TestCase):
    def test_island_perimeter(self):
        self.assertEqual(
            island_perimeter([[1]]),
            4,
        )

        self.assertEqual(
            island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]),
            16,
        )


if __name__ == "__main__":
    unittest.main()
