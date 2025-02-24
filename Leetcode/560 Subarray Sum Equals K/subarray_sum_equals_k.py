import unittest


# Time: O(n), where n => length of nums
# Space: O(n)
def subarray_sum_equals_k(nums, k):
    prefix_sum_count = {0: 1}
    res, prefix_sum = 0, 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_sum_count:
            res += prefix_sum_count[prefix_sum - k]

        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return res


class TestSubarraySumEqualsK(unittest.TestCase):
    def test_subarray_sum_equals_k(self):
        self.assertEqual(subarray_sum_equals_k([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum_equals_k([1, 2, 3], 3), 2)


if __name__ == "__main__":
    unittest.main()
