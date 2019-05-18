# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

"""
        0 1 2 3 4 5 6 7 8
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Area = length * width => (idx2 - idx1) * shorter_segment
                                ^           ^
                            Maximize    Maximize
Brute Force => O (n^2)
 for each i, j => j = i+1 -> len(arr):
     update max_area



Approach 2:

Always move shorter length 

 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
 l               r
 Area = 8

 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
   l             r
Area = 49

 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
   l           r
Area = 18

....

""" 


def max_area(arr):
    if len(arr) == 0 or len(arr) == 1: return None

    area = 0
    left, right = 0, len(arr) - 1

    while left < right:
        area = max(area, (right - left) * min(arr[left], arr[right]))
        if arr[left] < arr[right]: left += 1
        else: right -= 1

    return area

import unittest
class TestMaxAreaWater(unittest.TestCase):
    def test_invalid_ip(self):
        self.assertEqual(max_area([]), None)
        self.assertEqual(max_area([1]), None)

    def test_0_area_ip(self):
        self.assertEqual(max_area([0, 2]), 0)

    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

if __name__ == "__main__": unittest.main()