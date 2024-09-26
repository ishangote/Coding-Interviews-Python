import unittest


class NumArrayBruteForce:
    # Time: O(1)
    # Space: O(1)
    def __init__(self, nums):
        self.nums = nums

    # Time: O(n), where n => length of nums
    # Space: O(1)
    def sumRange(self, left, right):
        res = 0

        for idx in range(left, right + 1):
            res += self.nums[idx]

        return res


class NumArrayCaching:
    # Time: O(n^2)
    # Space: O(n^2)
    def __init__(self, nums):
        self.nums = nums
        self.range_sum = {}

        for idx1 in range(len(nums)):
            sum = 0
            for idx2 in range(idx1, len(nums)):
                sum += nums[idx2]
                self.range_sum[(idx1, idx2)] = sum

    # Time: O(1)
    # Space: O(1)
    def sumRange(self, left, right):
        return self.range_sum[(left, right)]


class NumArrayOptimized:
    # Time: O(n)
    # Space: O(n)
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sums = []

        sum = 0
        for num in nums:
            sum += num
            self.prefix_sums.append(sum)

    # Time: O(1)
    # Space: O(1)
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sums[right]

        return self.prefix_sums[right] - self.prefix_sums[left - 1]


class TestNumArray(unittest.TestCase):
    def test_num_array_bf(self):
        num_array = NumArrayBruteForce([-2, 0, 3, -5, 2, -1])

        self.assertEqual(num_array.sumRange(0, 2), 1)
        self.assertEqual(num_array.sumRange(2, 5), -1)
        self.assertEqual(num_array.sumRange(0, 5), -3)

    def test_num_array_cached(self):
        num_array = NumArrayCaching([-2, 0, 3, -5, 2, -1])

        self.assertEqual(num_array.sumRange(0, 2), 1)
        self.assertEqual(num_array.sumRange(2, 5), -1)
        self.assertEqual(num_array.sumRange(0, 5), -3)

    def test_num_array_optimized(self):
        num_array = NumArrayOptimized([-2, 0, 3, -5, 2, -1])

        self.assertEqual(num_array.sumRange(0, 2), 1)
        self.assertEqual(num_array.sumRange(2, 5), -1)
        self.assertEqual(num_array.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
