import unittest


def search_target_row(matrix, target):
    lo, hi = 0, len(matrix) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        if target > matrix[mid][-1]:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def search_target(row, target):
    lo, hi = 0, len(row) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target == mid:
            return True
        if target > mid:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


# Time: O(log(n) + log(m)), where n => number of rows in matrix, m => number of cols in matrix
# Space: O(1)
def search_2d_matrix_binary_search(matrix, target):
    target_row = search_target_row(matrix, target)
    return search_target(matrix[target_row], target)


class TestSearch2DMatrix(unittest.TestCase):
    def test_search_2d_matrix_binary_search(self):
        self.assertEqual(search_2d_matrix_binary_search([[1]], 2), False)
        self.assertEqual(
            search_2d_matrix_binary_search(
                [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3
            ),
            True,
        )
        self.assertEqual(
            search_2d_matrix_binary_search(
                [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13
            ),
            False,
        )
        self.assertEqual(
            search_2d_matrix_binary_search(
                [[-10, -8, -6, -4, -3], [0, 2, 3, 4, 5], [8, 9, 10, 10, 12]], 0
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
