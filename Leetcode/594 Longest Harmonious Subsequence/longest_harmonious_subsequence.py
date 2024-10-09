import unittest
from collections import Counter


# Time: O(nlogn), where n => length of nums
# Space: O(1)
def longest_harmonious_subsequence_sorting(nums):
    nums.sort()

    lo, hi, res = 0, 0, 0

    while hi < len(nums):
        if nums[hi] - nums[lo] == 0:
            hi += 1

        elif nums[hi] - nums[lo] == 1:
            res = max(res, hi - lo + 1)
            hi += 1

        else:
            lo += 1

    return res


# Time: O(n), where n => length of nums
# Space: O(n)
def longest_harmonious_subsequence_counting(nums):
    count_nums = Counter(nums)
    res = 0

    for num in count_nums:
        if num + 1 in count_nums:
            res = max(res, count_nums[num] + count_nums[num + 1])

    return res


class TestLongestHarmoniousSubSequence(unittest.TestCase):
    def test_longest_harmonious_subsequence_sorting(self):
        self.assertEqual(
            longest_harmonious_subsequence_sorting([1, 3, 2, 2, 5, 2, 3, 7]), 5
        )
        self.assertEqual(longest_harmonious_subsequence_sorting([1, 2, 3, 4]), 2)
        self.assertEqual(longest_harmonious_subsequence_sorting([1, 1, 1, 1]), 0)

    def test_longest_harmonious_subsequence_counting(self):
        self.assertEqual(
            longest_harmonious_subsequence_counting([1, 3, 2, 2, 5, 2, 3, 7]), 5
        )
        self.assertEqual(longest_harmonious_subsequence_counting([1, 2, 3, 4]), 2)
        self.assertEqual(longest_harmonious_subsequence_counting([1, 1, 1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
