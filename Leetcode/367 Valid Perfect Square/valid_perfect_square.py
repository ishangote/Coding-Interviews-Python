import unittest


# Time: O(log(num))
# Space: O(1)
def valid_perfect_square(num):
    if num < 2:
        return True

    lo, hi = 2, num // 2

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * mid == num:
            return True

        if mid * mid > num:
            hi = mid - 1

        else:
            lo = mid + 1

    return False


class TestValidPerfectSquare(unittest.TestCase):
    def test_valid_perfect_square(self):
        self.assertAlmostEqual(valid_perfect_square(1), True)
        self.assertAlmostEqual(valid_perfect_square(2), False)
        self.assertAlmostEqual(valid_perfect_square(3), False)
        self.assertAlmostEqual(valid_perfect_square(4), True)
        self.assertAlmostEqual(valid_perfect_square(5), False)
        self.assertAlmostEqual(valid_perfect_square(9), True)
        self.assertAlmostEqual(valid_perfect_square(16), True)


if __name__ == "__main__":
    unittest.main()
