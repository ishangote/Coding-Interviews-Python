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
----------------------------------------
Approach 3: Stacks
Instead of storing the largest bar upto an index as in Approach 2, 
we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water.
We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, 
which means that the current bar is bounded by the previous bar in the stack. 
If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is
bounded by the current bar and a previous bar in the stack, 
hence, we can pop it and add resulting trapped water to ans.

Water is trapped when an increasing height appears.

Time: O(n)
Space: O(n)
"""

def trapping_water_stack(heights):
    if not heights: return 0
    ans, stack = 0, []

    for i, v in enumerate(heights):
        while stack and heights[stack[-1]] < v:
            prev_bound = heights[stack.pop()]
            if not stack: break
            left_max = stack[-1]
            h = min(heights[left_max], v) - prev_bound
            w = i - left_max - 1
            ans += h * w

        stack.append(i)

    return ans

import unittest
class TestTrappingRainWater(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(trapping_water_stack([0, 1, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 5)

if __name__ == "__main__": unittest.main()