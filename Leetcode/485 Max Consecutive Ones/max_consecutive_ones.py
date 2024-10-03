import unittest
import sys


# Time: O(n), where n => length of nums
# Space: O(1)
def max_consecutive_ones(nums):
    count, max_count = 0, -sys.maxsize

    for num in nums:
        if num == 0:
            count = 0

        if num == 1:
            count += 1

        max_count = max(count, max_count)

    return max_count


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones(self):
        self.assertEqual(max_consecutive_ones([0, 0, 0]), 0)
        self.assertEqual(max_consecutive_ones([0, 1, 0]), 1)
        self.assertEqual(max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(max_consecutive_ones([1, 0, 1, 1, 0, 1]), 2)


if __name__ == "__main__":
    unittest.main()
