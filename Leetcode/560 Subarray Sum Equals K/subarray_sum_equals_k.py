import unittest


# Original function: Count the number of subarrays that sum to k.
# Time: O(n), where n is the length of nums
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


# ------------------------------------------------------------------------------------ #


# * Variation 1: Return True/False if any subarray sums to k.
# Time: O(n)
# Space: O(n)
def subarray_sum_equals_k_variation_boolean(nums, k):
    prefix_sum_set = {0}
    prefix_sum = 0
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_sum_set:
            return True
        prefix_sum_set.add(prefix_sum)
    return False


# ------------------------------------------------------------------------------------ #


# * Variation 2: For only non-negative numbers. Return count of subarrays summing to k.
# Time: O(n)
# Space: O(1)
def subarray_sum_equals_k_variation_positives_count(nums, k):
    start, cur_sum, res = 0, 0, 0
    for end in range(len(nums)):
        cur_sum += nums[end]
        # Shrink the window until the current sum is <= k.
        while start <= end and cur_sum > k:
            cur_sum -= nums[start]
            start += 1
        if cur_sum == k:
            res += 1
    return res


# ------------------------------------------------------------------------------------ #


# * Variation 3: For only non-negative numbers. Return maximum length of subarray summing to k.
# Time: O(n)
# Space: O(1)
def subarray_sum_equals_k_variation_positives_length(nums, k):
    start, cur_sum, res = 0, 0, 0
    for end in range(len(nums)):
        cur_sum += nums[end]
        # Shrink the window until the current sum is <= k.
        while start <= end and cur_sum > k:
            cur_sum -= nums[start]
            start += 1
        if cur_sum == k:
            res = max(res, end - start + 1)
    return res


# ------------------------------------------------------------------------------------ #
class TestSubarraySumEqualsK(unittest.TestCase):
    # Tests for the original prefix sum count function.
    def test_original(self):
        self.assertEqual(subarray_sum_equals_k([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum_equals_k([1, 2, 3], 3), 2)
        self.assertEqual(subarray_sum_equals_k([0, 0, 0], 0), 6)
        self.assertEqual(subarray_sum_equals_k([1, -1, 1, -1], 0), 4)

    # Tests for the Boolean variation.
    def test_variation_boolean(self):
        self.assertTrue(subarray_sum_equals_k_variation_boolean([1, 1, 1], 2))
        self.assertTrue(subarray_sum_equals_k_variation_boolean([1, 2, 3], 3))
        self.assertFalse(subarray_sum_equals_k_variation_boolean([1, 2, 3], 7))
        self.assertTrue(subarray_sum_equals_k_variation_boolean([0, 0, 0], 0))

    # Tests for the positives-only count variation.
    def test_variation_positives_count(self):
        # Only non-negative numbers; sliding window applies.
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_count([1, 2, 3], 3), 2
        )  # [1,2] and [3]
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_count([1, 1, 1, 1], 2), 3
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_count([2, 3, 1, 2, 4], 5), 1
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_count([1, 2, 3, 4, 5], 15), 1
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_count([1, 2, 3, 4, 5], 100), 0
        )

    # Tests for the positives-only maximum length variation.
    def test_variation_positives_length(self):
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_length([1, 2, 3], 3), 2
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_length([1, 1, 1, 1], 2), 2
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_length([1, 2, 1, 2, 3], 3), 2
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_length([1, 2, 3, 4, 5], 15), 5
        )
        self.assertEqual(
            subarray_sum_equals_k_variation_positives_length([1, 2, 3, 4, 5], 100), 0
        )


if __name__ == "__main__":
    unittest.main()
