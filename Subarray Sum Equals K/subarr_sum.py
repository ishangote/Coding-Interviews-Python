# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""

                [10, 2, -2, -20, 10]    k = -10
                                 ^
hm =
{
    0:2
    10:2
    12:1
    -10:1
}
count = 3
current_sum =   [10, 12, 10, -10, 0]
current_sum-k = [20, 22, 20, 0, 10]
"""

def subarray_sum(arr, k):
    hm, curr_sum, count = {0:1}, 0, 0

    for num in arr:
        curr_sum += num
        if curr_sum - k in hm:
            count += hm[curr_sum - k]
        
        if curr_sum not in hm: hm[curr_sum] = 1
        else: hm[curr_sum] += 1
        
    return count

import unittest
class TestSubArraySumEqualsK(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(subarray_sum([], 2), 0)

    def test_no_subarray_equals_k(self):
        self.assertEqual(subarray_sum([1, 2, 3, 4], -2), 0)

    def test_k_as_subarray(self):
        self.assertEqual(subarray_sum([-1, 3, -2, -6], 3), 1)

    def test_generic_input(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum([-1, 2, 3, -1, 6], 5), 2)
        self.assertEqual(subarray_sum([10, 2, -2, -20, 10], -10), 3)
        self.assertEqual(subarray_sum([9, 4, 20, 3, 10, 5], 33), 2)
        
if __name__ == "__main__": unittest.main()