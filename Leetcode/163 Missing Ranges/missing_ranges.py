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


# -------------------------------------------------------- #
# * Variation: Formatting Requirements (Return strings)


def missing_range_helper(lo, hi):
    if lo == hi:
        return [str(lo)]
    if hi - lo == 1:
        return [str(lo), str(hi)]
    else:
        return [f"{lo}->{hi}"]


# Time: O(n), where n => length of nums
# Space: O(1)
def missing_ranges_variation(nums, lower, upper):
    if not nums:
        return missing_range_helper(lower, upper)

    res = []

    if lower < nums[0]:
        res.extend(missing_range_helper(lower, nums[0] - 1))

    for idx in range(1, len(nums)):
        if nums[idx] - nums[idx - 1] == 1:
            continue
        res.extend(missing_range_helper(nums[idx - 1] + 1, nums[idx] - 1))

    if upper > nums[-1]:
        res.extend(missing_range_helper(nums[-1] + 1, upper))

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


class TestMissingRangesVariation(unittest.TestCase):
    def test_empty_nums(self):
        # When nums is empty, the missing range covers the whole interval.
        self.assertEqual(missing_ranges_variation([], 0, 0), ["0"])
        self.assertEqual(missing_ranges_variation([], 1, 1), ["1"])
        self.assertEqual(missing_ranges_variation([], 1, 2), ["1", "2"])
        self.assertEqual(missing_ranges_variation([], 1, 3), ["1->3"])

    def test_no_missing_ranges(self):
        # When there are no missing numbers.
        self.assertEqual(missing_ranges_variation([1, 2, 3], 1, 3), [])
        self.assertEqual(missing_ranges_variation([1, 2, 3, 4, 5], 1, 5), [])

    def test_missing_at_start(self):
        # Missing numbers before the first element.
        self.assertEqual(missing_ranges_variation([3, 4, 5], 1, 5), ["1", "2"])

    def test_missing_at_end(self):
        # Missing numbers after the last element.
        self.assertEqual(missing_ranges_variation([1, 2, 3], 1, 5), ["4", "5"])

    def test_missing_in_between(self):
        # Missing numbers between elements as well as before and after.
        self.assertEqual(
            missing_ranges_variation([1, 3, 50, 75], 0, 99),
            ["0", "2", "4->49", "51->74", "76->99"],
        )

    def test_adjacent_numbers(self):
        # When the gap consists of exactly two consecutive numbers.
        self.assertEqual(missing_ranges_variation([1, 4], 1, 4), ["2", "3"])

    def test_single_missing(self):
        # When exactly one number is missing.
        self.assertEqual(missing_ranges_variation([1, 3], 1, 3), ["2"])


if __name__ == "__main__":
    unittest.main()
