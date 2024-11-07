import unittest


def can_ship_capacity(capacity, weights, days):
    required_days = 1
    cur_load = 0

    for weight in weights:
        if cur_load + weight > capacity:
            required_days += 1
            cur_load = 0

        cur_load += weight

    return required_days <= days


# Time: O(nlogm), where n => length of weights, m => sum(weights)
# Space: O(1)
def ship_within_days(weights, days):
    lo, hi = max(weights), sum(weights)

    while lo < hi:
        mid_capacity = (lo + hi) // 2

        if can_ship_capacity(mid_capacity, weights, days):
            hi = mid_capacity
        else:
            lo = mid_capacity + 1

    return lo


class TestShipWithinDays(unittest.TestCase):
    def test_ship_within_days(self):
        self.assertEqual(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
        self.assertEqual(ship_within_days([3, 2, 2, 4, 1, 4], 3), 6)
        self.assertEqual(ship_within_days([1, 2, 3, 1, 1], 4), 3)
        self.assertEqual(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
        self.assertEqual(ship_within_days([3, 2, 2, 4, 1, 4], 3), 6)
        self.assertEqual(ship_within_days([1, 2, 3, 1, 1], 4), 3)
        self.assertEqual(ship_within_days([10, 50, 30, 20, 40], 2), 90)


if __name__ == "__main__":
    unittest.main()
