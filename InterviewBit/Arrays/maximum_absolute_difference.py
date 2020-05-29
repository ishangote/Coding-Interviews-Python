"""
Given an unsorted array A of N integers, A_{1}, A_{2}, ...., A_{N}. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) or absolute difference of two elements of an array A is defined as |A[i] – A[j]| + |i – j|, where |A| denotes
the absolute value of A.

Input : A = {1, 3, -1}
Output : 5
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
So, we return 5.

Input : A = {3, -2, 5, -4}
Output : 10
f(1, 1) = f(2, 2) = f(3, 3) = f(4, 4) = 0
f(1, 2) = f(2, 1) = |3 - (-2)| + |1 - 2| = 6
f(1, 3) = f(3, 1) = |3 - 5| + |1 - 3| = 4
f(1, 4) = f(4, 1) = |3 - (-4)| + |1 - 4| = 10
f(2, 3) = f(3, 2) = |(-2) - 5| + |2 - 3| = 8
f(2, 4) = f(4, 2) = |(-2) - (-4)| + |2 - 4| = 4
f(3, 4) = f(4, 3) = |5 - (-4)| + |3 - 4| = 10

Solution =>

# Case 1: A[i] > A[j] and i > j
# |A[i] - A[j]| = A[i] - A[j]
# |i -j| = i - j
# hence, f(i, j) = (A[i] + i) - (A[j] + j)

# Case 2: A[i] < A[j] and i < j
# |A[i] - A[j]| = -(A[i]) + A[j]
# |i -j| = -(i) + j
# hence, f(i, j) = -(A[i] + i) + (A[j] + j)

# Case 3: A[i] > A[j] and i < j
# |A[i] - A[j]| = A[i] - A[j]
# |i -j| = -(i) + j
# hence, f(i, j) = (A[i] - i) - (A[j] - j)

# Case 4: A[i] < A[j] and i > j
# |A[i] - A[j]| = -(A[i]) + A[j]
# |i -j| = i - j
# hence, f(i, j) = -(A[i] - i) + (A[j] - j)

C1 => (A[i] + i) - (A[j] + j)
C2 => -(A[i] + i) + (A[j] + j)
= abs((A[i] + i) - (A[j] + j))

To find => 
max_add = (A[i] + i)
min_add = (A[j] + j) 

OR

C3 => (A[i] - i) - (A[j] - j)
C4 => -(A[i] - i) + (A[j] - j)
= abs((A[i] - i) - (A[j] - j))

To find =>
max_diff = (A[i] - i)
min_diff = (A[j] - j)
"""
import sys
def max_absolute_difference(nums):
    max_add, min_add = -sys.maxsize, sys.maxsize
    max_diff, min_diff = -sys.maxsize, sys.maxsize
    
    for idx in range(len(nums)):
        max_add = max(max_add, nums[idx] + idx)
        min_add = min(min_add, nums[idx] + idx)
        
        max_diff = max(max_diff, nums[idx] - idx)
        min_diff = min(min_diff, nums[idx] - idx)
        
    return max(max_add - min_add, max_diff - min_diff)

import unittest
class TestMaxAbsoluteDifference(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(max_absolute_difference([55, -8, 43, 52, 8, 59, -91, -79, -18, -94]), 158)
        self.assertEqual(max_absolute_difference([3, -2, 5, -4]), 10)

if __name__ == '__main__': unittest.main()