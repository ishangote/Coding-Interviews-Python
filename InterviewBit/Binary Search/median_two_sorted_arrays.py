# There are two sorted arrays X and Y of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time compleXity should be O(log (m+n)).
# You may assume nums1 and Y cannot be both empty.
"""

Brute Force: Merege two arrays: O(x + y)

Example 1:
X = [1, 3]
Y = [2]

The median is 2.0
Example 2:

X = [1, 2]
Y = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
# O(log(min(len(X), len(Y))))
def median_of_arrays(X, Y):
    if len(Y) < len(X): X, Y = Y, X
    
    start, end = 0, len(X)

    while start <= end:
        px = (start + end) // 2
        py = ((len(X) + len(Y) + 1) // 2) - px

        leftx = -float('inf') if px == 0 else X[px - 1]
        rightx = float('inf') if px == len(X) else X[px]
        lefty = -float('inf') if py == 0 else Y[py - 1]
        righty = float('inf') if py == len(Y) else Y[py]

        if leftx <= righty and lefty <= rightx: return max(leftx, lefty) if (len(X) + len(Y)) % 2 != 0 else (max(leftx, lefty) + min(rightx, righty)) / 2
        elif leftx > righty: end = px - 1
        else: start = px + 1

import unittest
class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(median_of_arrays([1, 3, 8, 9, 16], [7, 11, 18, 19, 21, 25]), 11)
        self.assertEqual(median_of_arrays([23, 26, 31, 35], [3, 5, 7, 9, 11, 16]), 13.5)

if __name__ == "__main__": unittest.main()