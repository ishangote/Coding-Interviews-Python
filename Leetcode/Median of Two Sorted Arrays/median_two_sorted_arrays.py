"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

0  1  2   3   4   5
4, 7, 14, 18
2, 3, 11, 19, 21, 23
l         r

"""
#Binary Search on smaller array

def get_median(X, Y):
    if len(X) > len(Y): X, Y = Y, X

    lo, hi = 0, len(X)

    while lo <= hi:
        px = (lo + hi) // 2
        py = ((len(X) + len(Y) + 1) // 2) - px

        left_x = -float('inf') if px == 0 else X[px - 1]
        right_x = float('inf') if px == len(X) else X[px]

        left_y = -float('inf') if py == 0 else Y[py - 1]
        right_y = float('inf') if py == len(Y) else Y[py]

        if left_x <= right_y and left_y <= right_x: return max(left_x, left_y) if (len(X) + len(Y)) % 2 != 0 else (max(left_x, left_y) + min(right_x, right_y)) / 2
        if left_x > right_y: hi = px - 1
        else: lo = px + 1

import unittest
class MedianOfTwoSortedArrays(unittest.TestCase):
    def test_genric(self):
        self.assertEqual(get_median([1, 3, 8, 9, 15],[7, 11, 18, 19, 21, 25]), 11)
        self.assertEqual(get_median([1, 3],[2]), 2)
        self.assertEqual(get_median([1, 2],[3, 4]), 2.5)

if __name__ == "__main__": unittest.main()