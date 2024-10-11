import unittest


def calculate_average(nums):
    return sum(nums) // len(nums)


# Time: O(r x c), where r => number of rows in image and c => number of cols in image
# Space: O(r x c), not doing operations in-place
def image_smoother(image):
    res = [[0 for col in range(len(image[0]))] for row in range(len(image))]

    for row in range(len(image)):
        for col in range(len(image[0])):
            nums = [image[row][col]]
            for offset in [
                (0, 1),
                (1, 0),
                (1, 1),
                (0, -1),
                (-1, 0),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]:
                offset_row, offset_col = row + offset[0], col + offset[1]

                if 0 <= offset_row < len(image) and 0 <= offset_col < len(image[0]):
                    nums.append(image[offset_row][offset_col])

            res[row][col] = calculate_average(nums)  # Floor division result

    return res


class TestImageSmoother(unittest.TestCase):
    def test_image_smoother(self):
        self.assertEqual(
            image_smoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )
        self.assertEqual(
            image_smoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]),
            [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
        )


if __name__ == "__main__":
    unittest.main()
