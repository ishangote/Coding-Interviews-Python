import unittest


# Time: O(n), where n => length of nums
# Space: O(1)
def missing_ranges(nums, lower, upper):
    if not nums:
        return [[lower, upper]]

    res = []

    if lower < nums[0]:
        res.append([lower, nums[0] - 1])

    for idx in range(1, len(nums)):
        if nums[idx] - nums[idx - 1] == 1:
            continue

        res.append(
            [nums[idx - 1] + 1, nums[idx] - 1],
        )

    if upper > nums[-1]:
        res.append([nums[-1] + 1, upper])

    return res


class TestMissingRanges(unittest.TestCase):
    def test_missing_ranges_edge(self):
        self.assertEqual(
            missing_ranges([-1], -1, -1),
            [],
        )

        self.assertEqual(
            missing_ranges([], 1, 4),
            [[1, 4]],
        )

    def test_missing_ranges(self):
        self.assertEqual(
            missing_ranges([0, 1, 3, 50, 75], 0, 99),
            [[2, 2], [4, 49], [51, 74], [76, 99]],
        )

        self.assertEqual(
            missing_ranges([1, 3], 0, 9),
            [[0, 0], [2, 2], [4, 9]],
        )


if __name__ == "__main__":
    unittest.main()
