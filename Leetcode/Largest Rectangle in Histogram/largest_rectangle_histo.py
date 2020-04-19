# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.
"""
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10

Approach 1: 
Brute Force: height of the rectangle formed between any two bars will always be limited by the height of the shortest bar lying between them
For two pointers, calculate min height bar between them and calculate area

Time Complexity: O(n^3)
Space Complexity: O(1)

Approach 2: 
Better Brute Force: height of the rectangle formed between any two bars will always be limited by the height of the shortest bar lying between them
For two pointers, we can find the bar of minimum height for current pair by using the minimum height bar of the previous pair.

Time Complexity: O(n^2)
Space Complexity: O(1)

Approach 3: Stack:

Case 1:


"""
def largest_rectangle(heights):
# In cases when stack has only one element i.e. -1 then stack[-1] = -1 and so heights[stack[-1]] = heights[-1] = 0 
# because we appended 0 to heights and 0 is smaller than all other heights, 
# so popping will stop there and -1 will never be popped out of the stack and 
# so this works as a stopping criterion (instead of doing something like this if stack).
    heights.append(0)
    stack = [-1]
    ans = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)

    heights.pop()
    return ans

import unittest
class TestHappyNumber(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(largest_rectangle([1, 2, 3, 4, 5]), 9)
        self.assertEqual(largest_rectangle([5, 4, 3, 2, 1]), 9)

    def test_generic(self):
        self.assertEqual(largest_rectangle([2,1,5,6,2,3]), 10)
        self.assertEqual(largest_rectangle([6, 1, 4, 3, 4, 1]), 9)

if __name__ == "__main__": unittest.main()