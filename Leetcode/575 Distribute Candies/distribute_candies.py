import unittest


# Time: O(1)
# Space: O(1)
def distribute_candies(candies):
    candy_types = set(candies)
    candies_can_eat = len(candies) // 2

    return len(candy_types) if len(candy_types) <= candies_can_eat else candies_can_eat


class TestDistributeCandies(unittest.TestCase):
    def test_distribute_candies(self):
        self.assertEqual(distribute_candies([1, 1, 2, 2, 3, 3]), 3)
        self.assertEqual(distribute_candies([1, 1, 1, 1, 3, 3]), 2)
        self.assertEqual(distribute_candies([1, 1, 2, 1, 3, 4]), 3)


if __name__ == "__main__":
    unittest.main()
