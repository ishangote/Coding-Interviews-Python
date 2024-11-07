import unittest


def can_cut_ribbons(length, ribbons, k):
    # Count how many ribbons of a given length can be obtained
    count = sum(ribbon // length for ribbon in ribbons)
    return count >= k


# Time: O(nlogm), where n => number of ribbons, m => max(ribbons)
# Space: O(1)
def cutting_ribbons(ribbons, k):
    if sum(ribbons) < k:
        return 0

    lo, hi = 1, max(ribbons)

    while lo <= hi:
        mid_length = (lo + hi) // 2

        if can_cut_ribbons(mid_length, ribbons, k):
            lo = mid_length + 1
        else:
            hi = mid_length - 1

    return hi


class TestCuttingRibbons(unittest.TestCase):
    def test_cutting_ribbons(self):
        self.assertEqual(cutting_ribbons([9, 7, 5], 3), 5)
        self.assertEqual(cutting_ribbons([7, 5, 9], 4), 4)
        self.assertEqual(cutting_ribbons([5, 7, 9], 22), 0)
        self.assertEqual(cutting_ribbons([1, 1, 1, 1], 5), 0)


if __name__ == "__main__":
    unittest.main()
