# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

#APPROACH: https://www.youtube.com/watch?v=Uog2Jmyb3iY&t=64s
#SOLUTIONS: https://www.youtube.com/watch?v=lhzrp3Nbj-w&t=365s, https://www.youtube.com/watch?v=pq7Xon_VXeU
"""
Input: [0, 1, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 5

heights =>                              0   1   2   1   0   1   3   2   1   2   1

left max for each i          =>         0   1   2   2   2   2   3   3   3   3   3
right max for each i         =>         3   3   3   3   3   3   3   2   2   2   1 

[min(leftmax, rightmax) - height_i] =>  0   0   0   1   2   1   0   0   1   0   0

Goal: To find leftmax, rightmax =>

Approach 1: Brute Force
For each i move towards the left again to find the left_max and then to the right to find the right max
Time: O(n^2)
Space: O(1)
----------------------------------------
Approach 2: Dynamic Programming

One iteration to calclulate the left max array
One reverse iteration to calculate the right max array

Time: O(n + n) = O(n)
Space: O(n + n) = O(n)
"""

def trapping_water(heights):
    if not heights: return 0
    left_max = [0 for i in range(len(heights))]
    right_max = [0 for i in range(len(heights))]

    #Populate left max
    left_max[0] = heights[0]
    for i in range(1, len(left_max)):
        left_max[i] = max(heights[i], left_max[i - 1])

    #Populate right max
    right_max[-1] = heights[-1]
    for i in range(len(right_max) - 2, -1, -1):
        right_max[i] = max(heights[i], right_max[i + 1])

    ans = 0
    for i in range(len(heights)):
        ans += min(left_max[i], right_max[i]) - heights[i]

    return ans

import unittest
class TestTrappingRainWater(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(trapping_water([0, 1, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 5)

if __name__ == "__main__": unittest.main()