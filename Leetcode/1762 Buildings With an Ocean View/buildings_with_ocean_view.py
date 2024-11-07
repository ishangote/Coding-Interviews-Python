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


class TestBuildingsWithOceanView(unittest.TestCase):
    def test_buildings_with_ocean_view(self):
        self.assertEqual(buildings_with_ocean_view([4, 2, 3, 1]), [0, 2, 3])
        self.assertEqual(buildings_with_ocean_view([4, 3, 2, 1]), [0, 1, 2, 3])
        self.assertEqual(buildings_with_ocean_view([1, 2, 3, 4]), [3])
        self.assertEqual(buildings_with_ocean_view([1, 1, 1]), [2])


if __name__ == "__main__":
    unittest.main()
