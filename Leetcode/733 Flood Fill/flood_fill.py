import unittest


def recursive_helper(image, row, col, color, visited):
    if image[row][col] == color:
        return

    original_color = image[row][col]
    visited.add((row, col))

    for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (
            0 <= row + row_offset < len(image)
            and 0 <= col + col_offset < len(image[0])
            and (row + row_offset, col + col_offset) not in visited
            and image[row + row_offset][col + col_offset] == original_color
        ):
            recursive_helper(image, row + row_offset, col + col_offset, color, visited)

    image[row][col] = color


# Time: O(n x m), where n => number of rows, m => number of cols
# Space: O(1)
def flood_fill(image, sr, sc, color):
    recursive_helper(image, sr, sc, color, set())
    return image


class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        self.assertEqual(
            flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        )


if __name__ == "__main__":
    unittest.main()
