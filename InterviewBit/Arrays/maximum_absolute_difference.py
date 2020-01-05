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
"""
#O(n) uses properties of absolute difference

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

# case1 and case 2 output = abs((A[i] + i) - (A[j] + j)) = abs(-(A[i] + i) + (A[j] + j))
# case2 and case 3 output = same

def max_absolute_difference(nums):
    max1, min1 = -2147483648, +2147483647
    max2, min2 = -2147483648, +2147483647
    for i in range(len(nums)):
        max1 = max(max1, nums[i] + i)
        min1 = min(min1, nums[i] + i)

        max2 = max(max2, nums[i] - i)
        min2 = min(min2, nums[i] - i)
    
    return max(max1 - min1, max2 - min2)

import unittest
class TestMaxAbsoluteDifference(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(max_absolute_difference([55, -8, 43, 52, 8, 59, -91, -79, -18, -94]), 158)
        self.assertEqual(max_absolute_difference([3, -2, 5, -4]), 10)

if __name__ == '__main__': unittest.main()