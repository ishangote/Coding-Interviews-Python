import unittest
from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window_sum, self.nums = 0, deque([])

    # Time: O(1)
    # Space: O(n), where n => size
    def next(self, value):
        self.nums.append(value)
        self.window_sum += value

        if len(self.nums) == self.size + 1:
            prev_number = self.nums.popleft()
            self.window_sum -= prev_number

        return self.window_sum / len(self.nums)


class TestMovingAverage(unittest.TestCase):
    def test_moving_average(self):
        moving_average = MovingAverage(3)

        self.assertEqual(moving_average.next(1), 1)
        self.assertEqual(moving_average.next(10), 5.5)
        self.assertAlmostEqual(moving_average.next(3), 4.66667, places=5)
        self.assertEqual(moving_average.next(5), 6)


if __name__ == "__main__":
    unittest.main()
