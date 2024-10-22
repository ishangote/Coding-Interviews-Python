import unittest


# Time: O(n), where n => number of levels
# Space: O(1)
def minimum_health(damage, armor):
    total_damage = sum(damage)
    max_damage = max(damage)
    total_damage -= min(max_damage, armor)
    return total_damage + 1


class TestMinimumHealth(unittest.TestCase):
    def test_minimum_health(self):
        self.assertEqual(minimum_health([2, 7, 4, 3], 4), 13)
        self.assertEqual(minimum_health([3, 3, 3], 0), 10)
        self.assertEqual(minimum_health([2, 5, 3, 4], 7), 10)


if __name__ == "__main__":
    unittest.main()
