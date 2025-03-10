import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    res = 1

    for num in nums:
        lo, hi = num - 1, num

        while hi in nums_set:
            nums_set.remove(hi)
            hi += 1

        while lo in nums_set:
            nums_set.remove(lo)
            lo -= 1

        res = max(res, hi - lo - 1)

    return res


class LongestConsecutiveSequence(unittest.TestCase):
    def test_longest_consecutive_sequence(self):
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(
            longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9
        )
        self.assertEqual(longest_consecutive_sequence([1, 0, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
