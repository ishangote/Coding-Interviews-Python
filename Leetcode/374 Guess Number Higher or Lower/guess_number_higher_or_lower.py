import unittest
from unittest.mock import patch


def guess():
    pass


# Time: O(logn)
# Space: O(1)
def guess_number(n):
    lo, hi = 1, n

    while lo <= hi:
        mid = (lo + hi) // 2

        is_guess_right = guess(mid)

        if is_guess_right == 0:
            return mid

        if is_guess_right == -1:
            hi = mid - 1

        if is_guess_right == 1:
            lo = mid + 1


class TestGuessNumber(unittest.TestCase):
    def test_guess_number(self):
        with patch("__main__.guess") as mock_guess:
            mock_guess.side_effect = lambda x: 0 if x == 6 else (1 if x < 6 else -1)

            self.assertEqual(guess_number(10), 6)

        with patch("__main__.guess") as mock_guess:
            mock_guess.side_effect = lambda x: 0 if x == 3 else (1 if x < 3 else -1)

            self.assertEqual(guess_number(10), 3)


if __name__ == "__main__":
    unittest.main()
