"""
nums1: [4, 6, 7, 0, 0] m = 3
              ^     ^
              m     p
nums2: [1, 3] n = 2
           ^
           n

"""

def merge_arrays(nums1, m, nums2, n):
    p = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:

        if nums1[m] > nums2[n]:
            nums1[p] = nums1[m]
            m -= 1
        else:
            nums1[p] = nums2[n]
            n -= 1

        p -= 1

    nums1[:n + 1] = nums2[:n + 1]
    return nums1

import unittest
class TestMergeSortedArrays(unittest.TestCase):
    def test_nums1_nums2_empty(self):
        self.assertEqual(merge_arrays([], 0, [], 0), [])
        self.assertEqual(merge_arrays([1, 2, 3], 3, [], 0), [1, 2, 3])
        self.assertEqual(merge_arrays([0, 0, 0], 0, [1, 2, 3], 3), [1, 2, 3])

    def test_merge_arrays(self):
        self.assertEqual(merge_arrays([1, 3, 6, 7, 0, 0, 0], 4, [5, 16, 21], 3), [1, 3, 5, 6, 7, 16, 21])
        self.assertEqual(merge_arrays([1, 18, 21, 0, 0, 0], 3, [5, 16, 21], 3), [1, 5, 16, 18, 21, 21])

if __name__ == "__main__": unittest.main()