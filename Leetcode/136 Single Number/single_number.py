from collections import Counter
import unittest


# Time: O(n)
# Space: O(n)
def single_number_optimized_time(nums):
    count_map = Counter(nums)

    for num in count_map:
        if count_map[num] == 1:
            return num


# Time: O(n)
# Space: O(1)
def single_number_optimized_time_space(nums):
    res = nums[0]

    for idx in range(1, len(nums)):
        res = res ^ nums[idx]

    return res


class TestSingleNumber(unittest.TestCase):
    def test_single_number_optimized_time(self):
        self.assertEqual(single_number_optimized_time([1]), 1)
        self.assertEqual(single_number_optimized_time([2, 2, 1]), 1)
        self.assertEqual(single_number_optimized_time([4, 1, 2, 1, 2]), 4)

    def test_single_number_optimized_time_space(self):
        self.assertEqual(single_number_optimized_time_space([1]), 1)
        self.assertEqual(single_number_optimized_time_space([2, 2, 1]), 1)
        self.assertEqual(single_number_optimized_time_space([4, 1, 2, 1, 2]), 4)


if __name__ == "__main__":
    unittest.main()
