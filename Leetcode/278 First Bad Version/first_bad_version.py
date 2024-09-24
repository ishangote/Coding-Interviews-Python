import unittest
from unittest.mock import patch


def isBadVersion(n):
    pass


# Time: O(log(n))
# Space: O(1)
def first_bad_version(n):
    lo, hi = 1, n

    while lo < hi:
        mid = (lo + hi) // 2
        is_mid_bad = isBadVersion(mid)

        if not is_mid_bad:
            lo = mid + 1
        else:
            hi = mid

    return lo


class TestFirstBadVersion(unittest.TestCase):
    def test_first_bad_version(self):
        with patch("__main__.isBadVersion") as mock_isBadVersion:
            mock_isBadVersion.side_effect = lambda n: n >= 4

            self.assertEqual(first_bad_version(5), 4)

        with patch("__main__.isBadVersion") as mock_isBadVersion:
            mock_isBadVersion.side_effect = lambda n: n >= 2

            self.assertEqual(first_bad_version(3), 2)


if __name__ == "__main__":
    unittest.main()
