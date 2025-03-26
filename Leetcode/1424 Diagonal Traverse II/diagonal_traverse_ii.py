import unittest
from collections import defaultdict, deque


# Time: O(n), where n => total number of elements in nums
# Space: O(n)
def diagonal_traverse_ii_hash_map(nums):
    diagonal_elements = defaultdict(list)
    max_diagonal_key = 0

    for row in range(len(nums) - 1, -1, -1):
        for col in range(len(nums[row]) - 1, -1, -1):
            max_diagonal_key = max(max_diagonal_key, row + col)
            diagonal_elements[row + col].append(nums[row][col])

    res = []
    for key in range(0, max_diagonal_key + 1):
        res.extend(diagonal_elements[key])

    return res


# Time: O(n), where n => total number of elements in nums
# Space: O(n)
def diagonal_traverse_ii_bfs(nums):
    queue = deque([(0, 0)])
    # Add to visited immediately after element is enqueued
    visited = {(0, 0)}
    res = []

    while queue:
        row, col = queue.pop()
        res.append(nums[row][col])

        next_row, next_col = row + 1, col + 1

        # Ensure the next row exists and that the current column index is
        # valid for that next row (handles jagged arrays)
        if (
            next_row < len(nums)
            and col < len(nums[next_row])
            and (next_row, col) not in visited
        ):
            queue.appendleft((next_row, col))
            visited.add((next_row, col))

        if next_col < len(nums[row]) and (row, next_col) not in visited:
            queue.appendleft((row, next_col))
            visited.add((row, next_col))

    return res


# Anti Diagonal
def diagonal_traverse_ii_variation1(nums):
    pass


class TestDiagonalTraverseII(unittest.TestCase):
    def test_diagonal_traverse_ii(self):
        self.assertEqual(
            diagonal_traverse_ii_hash_map(
                [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
            ),
            [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        )
        self.assertEqual(
            diagonal_traverse_ii_hash_map([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 4, 2, 7, 5, 3, 8, 6, 9],
        )
        self.assertEqual(
            diagonal_traverse_ii_hash_map(
                [[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]]
            ),
            [14, 13, 12, 11, 14, 19, 13, 15, 16, 1, 8, 9, 11],
        )

    def test_diagonal_traverse_ii_bfs(self):
        self.assertEqual(
            diagonal_traverse_ii_bfs(
                [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
            ),
            [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        )
        self.assertEqual(
            diagonal_traverse_ii_bfs([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 4, 2, 7, 5, 3, 8, 6, 9],
        )
        self.assertEqual(
            diagonal_traverse_ii_bfs(
                [[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]]
            ),
            [14, 13, 12, 11, 14, 19, 13, 15, 16, 1, 8, 9, 11],
        )


if __name__ == "__main__":
    unittest.main()
