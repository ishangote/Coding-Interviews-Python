import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def two_sum(nums, target):
    hash_map = {}
    for idx in range(len(nums)):
        if target - nums[idx] in hash_map:
            return [hash_map[target - nums[idx]], idx]

        hash_map[nums[idx]] = idx

    return []


# * Variation: Return True/False (Multiple Answers Exist)
# Time: O(n), where n => length of nums
# Space: O(n)
def two_sum_variation(nums, target):
    hash_set = set()
    for num in nums:
        if target - num in hash_set:
            return True

        hash_set.add(num)

    return False


class TestTwoSumUnitTest(unittest.TestCase):
    def test_two_sum_no_pair(self):
        self.assertEqual(two_sum([1, 3, 7, 5], 3), [])

    def test_two_sum_negative_nums(self):
        self.assertEqual(two_sum([-2, 4, 1, -3, 3], 1), [1, 3])

    def two_sum_generic(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])


if __name__ == "__main__":
    unittest.main()
