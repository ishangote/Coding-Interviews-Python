import unittest


def recursive_helper(row, col, visited, heights):
    displacement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited.add((row, col))

    for disp in displacement:
        new_row, new_col = row + disp[0], col + disp[1]
        if (
            0 <= new_row < len(heights)
            and 0 <= new_col < len(heights[0])
            and (new_row, new_col) not in visited
            and heights[new_row][new_col] >= heights[row][col]
        ):
            recursive_helper(new_row, new_col, visited, heights)


# Time: O(m * n), where m => number of rows, n => number of cols
# Space: O(m * n)
def pacific_atlantic_water_flow(heights):
    visited_from_pacific = set()
    visited_from_atlantic = set()

    for row in range(len(heights)):
        recursive_helper(row, 0, visited_from_pacific, heights)
        recursive_helper(row, len(heights[0]) - 1, visited_from_atlantic, heights)

    for col in range(len(heights[0])):
        recursive_helper(0, col, visited_from_pacific, heights)
        recursive_helper(len(heights) - 1, col, visited_from_atlantic, heights)

    return [
        list(coord)
        for coord in visited_from_pacific.intersection(visited_from_atlantic)
    ]


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def test_pacific_atlantic_water_flow(self):
        self.assertEqual(
            sorted(
                pacific_atlantic_water_flow(
                    [
                        [1, 2, 2, 3, 5],
                        [3, 2, 3, 4, 4],
                        [2, 4, 5, 3, 1],
                        [6, 7, 1, 4, 5],
                        [5, 1, 1, 2, 4],
                    ]
                )
            ),
            sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
        )
        self.assertEqual(
            pacific_atlantic_water_flow([[1, 1], [1, 1], [1, 1]]),
            [[0, 1], [2, 1], [0, 0], [1, 1], [2, 0], [1, 0]],
        )
        self.assertEqual(
            pacific_atlantic_water_flow([[1]]),
            [[0, 0]],
        )


if __name__ == "__main__":
    unittest.main()
