import unittest


# Time: O(n), where n => length of heights
# Space: O(1)
def container_with_most_water(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    res = 0

    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        res = max(res, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return res


class TestMaxAreaWater(unittest.TestCase):
    def test_invalid_ip(self):
        self.assertEqual(container_with_most_water([]), 0)
        self.assertEqual(container_with_most_water([1]), 0)

    def test_0_area_ip(self):
        self.assertEqual(container_with_most_water([0, 2]), 0)

    def test_max_area(self):
        self.assertEqual(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == "__main__":
    unittest.main()
