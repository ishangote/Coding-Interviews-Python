import unittest
from collections import deque


# Time: O(n^2), where n => length of grid
# Space: O(n^2)
def shortest_path_in_binary_matrix(grid):
    if grid[0][0] != 0:
        return -1

    queue = deque([(0, 0, 1)])
    visited = set((0, 0))
    displacements = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    while queue:
        (row, col, dist) = queue.pop()

        if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
            return dist

        for disp_row, disp_col in displacements:
            next_row, next_col = row + disp_row, col + disp_col
            if (
                0 <= next_row < len(grid)
                and 0 <= next_col < len(grid[0])
                and (next_row, next_col) not in visited
                and grid[next_row][next_col] == 0
            ):
                visited.add((next_row, next_col))
                queue.appendleft((next_row, next_col, dist + 1))

    return -1


# * Variation 1: Return the path coordinates -> Remember Time Complexity
# Time: O(n^3) => In the worst case, each cell's path (up to O(n^2) in length) is copied during BFS.
# Space: O(n^2)
def shortest_path_in_binary_matrix_variation(grid):
    if grid[0][0] == 1:
        return []

    queue = deque([(0, 0, [(0, 0)])])
    visited = set((0, 0))
    displacements = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    while queue:
        row, col, cur_path = queue.pop()
        if row == col == len(grid) - 1:
            return cur_path

        for row_dir, col_dir in displacements:
            next_row, next_col = row + row_dir, col + col_dir

            if (
                0 <= next_row < len(grid)
                and 0 <= next_col < len(grid[0])
                and (next_row, next_col) not in visited
                and grid[next_row][next_col] == 0
            ):
                visited.add((next_row, next_col))
                next_path = cur_path + [(next_row, next_col)]
                queue.appendleft((next_row, next_col, next_path))

    return []


class TestShortestPathInBinaryMatrix(unittest.TestCase):
    def test_shortest_path_in_binary_matrix(self):
        self.assertEqual(
            shortest_path_in_binary_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]]), -1
        )

        self.assertEqual(
            shortest_path_in_binary_matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), -1
        )

        self.assertEqual(
            shortest_path_in_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1
        )

        self.assertEqual(
            shortest_path_in_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4
        )

    def test_shortest_path_in_binary_matrix_variation(self):
        # Test when the starting cell is blocked.
        grid_blocked_start = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(
            shortest_path_in_binary_matrix_variation(grid_blocked_start), []
        )

        # Test when the ending cell is blocked.
        grid_blocked_end = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        self.assertEqual(shortest_path_in_binary_matrix_variation(grid_blocked_end), [])

        # Test a valid grid with a valid path from (0,0) to (2,2).
        grid_valid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        path = shortest_path_in_binary_matrix_variation(grid_valid)
        self.assertNotEqual(path, [], "Expected a valid path but got an empty list.")
        self.assertEqual(path[0], (0, 0), "Path should start at (0,0).")
        self.assertEqual(path[-1], (2, 2), "Path should end at (2,2).")

        # Test a single-cell grid.
        grid_single = [[0]]
        self.assertEqual(
            shortest_path_in_binary_matrix_variation(grid_single), [(0, 0)]
        )


if __name__ == "__main__":
    unittest.main()
