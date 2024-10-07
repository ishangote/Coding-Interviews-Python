import unittest
from math import sqrt


# Time: O(n), where n = area
# Space: O(1)
def construct_rectangle_brute_force(area):
    width, length = 1, area
    res = [length, width]

    while length >= width:
        current_area = width * length

        if current_area == area:
            res = [length, width]
            width += 1
            length -= 1

        elif current_area > area:
            length -= 1

        else:
            width += 1

    return res


# Time: O(sqrt(n)), where n = area
def construct_rectangle_optimized(area):
    for width in range(int(sqrt(area)), 0, -1):
        if area % width == 0:
            length = area // width
            return [length, width]


class TestConstructRectangle(unittest.TestCase):
    def test_construct_rectangle(self):
        self.assertEqual(construct_rectangle_brute_force(4), [2, 2])
        self.assertEqual(construct_rectangle_brute_force(37), [37, 1])
        self.assertEqual(construct_rectangle_brute_force(122122), [427, 286])


if __name__ == "__main__":
    unittest.main()
