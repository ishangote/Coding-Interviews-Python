import unittest
import math


def is_speed_valid(speed, piles, h):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile / speed)
        if hours > h:
            return False

    return True


# Time: O(log(m) * n), where m => max(piles) and n => length of piles
# Space: O(1)
def koko_eating_bananas(piles, h):
    lo, hi = 1, max(piles)

    while lo < hi:
        mid = (lo + hi) // 2
        if is_speed_valid(mid, piles, h):
            hi = mid
        else:
            lo = mid + 1

    return lo


class TestKokoEatingBananas(unittest.TestCase):
    def test_koko_eating_bananas(self):
        self.assertEqual(koko_eating_bananas([3, 6, 7, 11], 8), 4)
        self.assertEqual(koko_eating_bananas([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(koko_eating_bananas([30, 11, 23, 4, 20], 6), 23)


if __name__ == "__main__":
    unittest.main()
