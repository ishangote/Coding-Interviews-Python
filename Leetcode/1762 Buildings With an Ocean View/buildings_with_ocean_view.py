import unittest

# * Problem: Next Greater
# * Traversal Direction: Left to Right
# * Stack Type: Decreasing


# Time: O(n), where n => length of heights
# Space: O(1)
def buildings_with_ocean_view(heights):
    stack = []

    for idx, height in enumerate(heights):
        while stack and heights[stack[-1]] <= height:
            stack.pop()

        stack.append(idx)

    return stack


# ---------------------------------------------------- #


# * Variation 1: Return count of buildings with ocean view (no auxiliary space)
# Time: O(n)
# Space: O(1)
def count_buildings_with_ocean_view(heights):
    max_height = heights[-1]
    res = 1

    for idx in range(len(heights) - 2, -1, -1):
        if heights[idx] > max_height:
            res += 1
            max_height = heights[idx]

    return res


# ---------------------------------------------------- #


# * Variation 2: Ocean is not only on right side. It can be on left side as well. Return indices
# * of buildings with ocean view either on left or right or both sides.

# TODO: Implement Variation 2


def buildings_with_ocean_view_variation_2(heights):
    pass


# ---------------------------------------------------- #


class TestBuildingsWithOceanView(unittest.TestCase):
    def test_buildings_with_ocean_view(self):
        self.assertEqual(buildings_with_ocean_view([4, 2, 3, 1]), [0, 2, 3])
        self.assertEqual(buildings_with_ocean_view([4, 3, 2, 1]), [0, 1, 2, 3])
        self.assertEqual(buildings_with_ocean_view([1, 2, 3, 4]), [3])
        self.assertEqual(buildings_with_ocean_view([1, 1, 1]), [2])


class TestCountBuildingsWithOceanView(unittest.TestCase):
    def test_buildings_with_ocean_view(self):
        self.assertEqual(count_buildings_with_ocean_view([4, 2, 3, 1]), 3)
        self.assertEqual(count_buildings_with_ocean_view([4, 3, 2, 1]), 4)
        self.assertEqual(count_buildings_with_ocean_view([1, 2, 3, 4]), 1)
        self.assertEqual(count_buildings_with_ocean_view([1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
