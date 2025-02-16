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


if __name__ == "__main__":
    unittest.main()
