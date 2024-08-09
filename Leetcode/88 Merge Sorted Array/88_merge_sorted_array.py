"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input:
          e
 0  1  2  3
[5, 6, 0, 0] (n = 2)
^

 0  1
[2, 4] (m = 3)
^

Process:
 0  1  2  3
[5, 6, 5, 6]
    e

 0  1  2  3
[2, 4, 5, 6]
e

Output: [2, 4, 5, 6]


Example 2:

Input:
 0  1  2
[1, 0, 0]
 ^

 0  1
[3, 4]
^

Process:
 0  1  2
[1, 3, 4]
e

Output:
[1, 3, 4]


Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 
Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

def merge_sorted_array(nums1, len1, nums2, len2):
    pt1, pt2, current = len1 - 1, len2 - 1, (len1 + len2) - 1

    while pt1 >= 0 and pt2 >= 0:
        if nums1[pt1] >= nums2[pt2]:
            nums1[current] = nums1[pt1]
            pt1 -= 1
        else:
            nums1[current] = nums2[pt2]
            pt2 -= 1
        
        current -= 1
    
    while pt1 >= 0:
        nums1[current] = nums1[pt1]
        pt1 -= 1
        current -= 1

    while pt2 >= 0:
        nums1[current] = nums2[pt2]
        pt2 -= 1
        current -= 1

    return

import unittest
class TestMergeSortedArray(unittest.TestCase):
    def test_nums1_empty(self):
        nums1, len1 = [0, 0, 0], 0
        nums2, len2 = [2, 3, 4], 3

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [2, 3, 4])

    def test_nums2_empty(self):
        nums1, len1 = [2, 3, 4], 0
        nums2, len2 = [], 0

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [2, 3, 4])

    def test_merge_sorted_array_example1(self):
        nums1, len1 = [1, 2, 3, 0, 0, 0], 3
        nums2, len2 = [2, 5, 6], 3

        merge_sorted_array(nums1, len1, nums2, len2)

        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

if __name__ == "__main__": unittest.main()