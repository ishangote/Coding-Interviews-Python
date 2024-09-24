import unittest


# Time: O(n)
# Space: O(1)
def summary_ranges(nums):
    ranges = []
    idx = 0

    while idx < len(nums):
        runner = idx + 1
        while runner < len(nums) and nums[runner] == nums[runner - 1] + 1:
            runner += 1

        current_range = (
            [str(nums[idx]), str(nums[runner - 1])]
            if nums[idx] != nums[runner - 1]
            else [str(nums[idx])]
        )

        ranges.append(current_range)
        idx = runner

    return ["->".join(current_range) for current_range in ranges]


class TestSummaryRanges(unittest.TestCase):
    def test_summary_ranges_edge(self):
        self.assertEqual(summary_ranges([99]), ["99"])

    def test_summary_ranges(self):
        self.assertEqual(
            summary_ranges([0, 2, 3, 4, 6, 8, 9]), ["0", "2->4", "6", "8->9"]
        )

        self.assertEqual(summary_ranges([0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"])


if __name__ == "__main__":
    unittest.main()
