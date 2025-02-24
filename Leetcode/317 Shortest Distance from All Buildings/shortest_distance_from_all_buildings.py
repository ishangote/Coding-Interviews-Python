import unittest
import sys
from collections import deque


def bfs_helper(grid, distance_grid, reach_grid, row, col, empty_land):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(row, col, 0)])

    while queue:
        row, col, distance = queue.pop()

        for row_dir, col_dir in DIRECTIONS:
            new_row, new_col = row + row_dir, col + col_dir
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and grid[new_row][new_col]
                == empty_land  # Only process the correct empty land
            ):
                grid[new_row][new_col] -= 1  # Mark as visited for this BFS run
                distance_grid[new_row][new_col] += distance + 1
                reach_grid[new_row][new_col] += 1
                queue.appendleft((new_row, new_col, distance + 1))


def min_distance_helper(distance_grid, reach_grid, total_buildings):
    min_distance = sys.maxsize

    for row in range(len(distance_grid)):
        for col in range(len(distance_grid[0])):
            if reach_grid[row][col] == total_buildings:
                min_distance = min(min_distance, distance_grid[row][col])

    return min_distance if min_distance != sys.maxsize else -1


# Time: O(B * m * n), where B => total buildings, m => number of rows, n => number of cols
# Space: O(m * n)
def shortest_distance_from_all_buildings(grid):
    empty_land, BUILDING = 0, 1

    buildings = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == BUILDING
    ]
    total_buildings = len(buildings)

    distance_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    reach_grid = [[0] * len(grid[0]) for _ in range(len(grid))]

    for row, col in buildings:
        bfs_helper(grid, distance_grid, reach_grid, row, col, empty_land)
        empty_land -= 1  # Reduce the value for the next BFS iteration

    return min_distance_helper(distance_grid, reach_grid, total_buildings)


def debug_grids(grid, distance_grid, reach_grid):
    print("Grid State:")
    for row in grid:
        print(row)
    print("\nDistance Grid:")
    for row in distance_grid:
        print(row)
    print("\nReach Grid:")
    for row in reach_grid:
        print(row)


class TestShortestDistanceFromAllBuildings(unittest.TestCase):
    def test_shortest_distance_from_all_buildings(self):
        self.assertEqual(
            shortest_distance_from_all_buildings(
                [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
            ),
            7,
        )

        self.assertEqual(
            shortest_distance_from_all_buildings(
                [[1, 0, 0, 1], [0, 2, 0, 0], [0, 0, 0, 1]]
            ),
            6,
        )

        self.assertEqual(
            shortest_distance_from_all_buildings(
                [[0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
            ),
            6,
        )

        self.assertEqual(
            shortest_distance_from_all_buildings([[1, 0], [0, 1]]),
            2,
        )

        self.assertEqual(
            shortest_distance_from_all_buildings([[1, 2, 0], [0, 2, 1], [0, 0, 0]]),
            5,
        )

        self.assertEqual(
            shortest_distance_from_all_buildings([[1]]),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
