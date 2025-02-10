import unittest


# Time: O(n), where n => length of heights
# Space: O(n)
def trapping_rain_water_dp(heights):
    left_max = [heights[0]] + [0] * (len(heights) - 1)
    right_max = [0] * (len(heights) - 1) + [heights[-1]]
    res = 0

    for idx in range(1, len(heights)):
        left_max[idx] = max(left_max[idx - 1], heights[idx])

    for idx in range(len(heights) - 2, -1, -1):
        right_max[idx] = max(right_max[idx + 1], heights[idx])

    for left, right, height in zip(left_max, right_max, heights):
        res += min(left, right) - height

    return res


# Time: O(n), where n => length of heights
# Space: O(1)
def trapping_rain_water_two_pointers(heights):
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[0], heights[-1]
    res = 0

    while left < right:
        if left_max <= right_max:
            res += left_max - heights[left]
            left += 1
            left_max = max(left_max, heights[left])
        else:
            res += right_max - heights[right]
            right -= 1
            right_max = max(right_max, heights[right])

    return res


class TestTrappingRainWater(unittest.TestCase):
    def test_trapping_rain_water_dp(self):
        self.assertEqual(trapping_rain_water_dp([0, 1, 0]), 0)
        self.assertEqual(trapping_rain_water_dp([1, 1, 1]), 0)
        self.assertEqual(trapping_rain_water_dp([0, 1, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 5)
        self.assertEqual(trapping_rain_water_dp([4, 2, 0, 3, 2, 5]), 9)
        self.assertEqual(trapping_rain_water_dp([3, 0, 5, 0, 4]), 7)

    def test_trapping_rain_water_two_pointers(self):
        self.assertEqual(trapping_rain_water_two_pointers([0, 1, 0]), 0)
        self.assertEqual(trapping_rain_water_two_pointers([1, 1, 1]), 0)
        self.assertEqual(
            trapping_rain_water_two_pointers([0, 1, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 5
        )
        self.assertEqual(trapping_rain_water_two_pointers([4, 2, 0, 3, 2, 5]), 9)
        self.assertEqual(trapping_rain_water_two_pointers([3, 0, 5, 0, 4]), 7)


if __name__ == "__main__":
    unittest.main()
