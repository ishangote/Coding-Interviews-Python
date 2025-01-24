import unittest
import sys


# Time: O(n*w), where n => number of books, w => shelf width
# Space: O(n)
def filling_bookcase_shelves_recursive(books, shelf_width):
    def recursive_helper(idx):
        if idx == len(books):
            return 0

        if idx in memo:
            return memo[idx]

        cur_shelf_width = shelf_width
        shelf_height = 0

        memo[idx] = sys.maxsize

        for itr in range(idx, len(books)):
            width, height = books[itr]

            if cur_shelf_width < width:
                break

            cur_shelf_width -= width
            shelf_height = max(shelf_height, height)

            memo[idx] = min(memo[idx], shelf_height + recursive_helper(itr + 1))

        return memo[idx]

    memo = {}
    return recursive_helper(0)


# Time: O(n*w), where n => number of books, w => shelf width
# Space: O(n)
def filling_bookcase_shelves_dp(books, shelf_width):
    memo = [0] * (len(books) + 1)

    for idx in range(len(books) - 1, -1, -1):
        cur_shelf_width = shelf_width
        shelf_height = 0

        memo[idx] = sys.maxsize

        for itr in range(idx, len(books)):
            width, height = books[itr]

            if cur_shelf_width < width:
                break

            cur_shelf_width -= width
            shelf_height = max(shelf_height, height)

            memo[idx] = min(memo[idx], memo[itr + 1] + shelf_height)

    return memo[0]


class TestFillingBookcaseShelves(unittest.TestCase):
    def test_filling_bookcase_shelves_recursive(self):
        self.assertEqual(
            filling_bookcase_shelves_recursive(
                [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
            ),
            6,
        )
        self.assertEqual(
            filling_bookcase_shelves_recursive([[1, 3], [2, 4], [3, 2]], 6),
            4,
        )

    def test_filling_bookcase_shelves_dp(self):
        self.assertEqual(
            filling_bookcase_shelves_dp(
                [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
            ),
            6,
        )
        self.assertEqual(
            filling_bookcase_shelves_dp([[1, 3], [2, 4], [3, 2]], 6),
            4,
        )


if __name__ == "__main__":
    unittest.main()
