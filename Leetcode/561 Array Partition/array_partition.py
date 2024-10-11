import unittest


# Time: O(nlogn), where n => length of nums
# Space: O(1)
def array_partition_sorting(nums):
    nums.sort()
    res = 0

    for idx in range(0, len(nums), 2):
        res += nums[idx]

    return res


class TestArrayPartition(unittest.TestCase):
    def test_array_partition(self):
        self.assertEqual(array_partition_sorting([1, 4, 3, 2]), 4)
        self.assertEqual(array_partition_sorting([6, 2, 6, 5, 1, 2]), 9)


if __name__ == "__main__":
    unittest.main()
