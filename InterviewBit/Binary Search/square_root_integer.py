# Implement int sqrt(int x).
# Compute and return the square root of x.
# If x is not a perfect square, return floor(sqrt(x))
"""
Example :
Input : 11
Output : 3


0 => 0
1 => 1


7 => sqrt lies between 1, 7

number in between 0 and 1:
0.6 => 0, 1
But we have been given integers only so no need for this test case

"""
def sqrt_bin_search(n):
    if n == 0  or n == 1: return n
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n: left = mid + 1
        else: right = mid - 1
    
    return right

import unittest
class TestSquareRootOfInteger(unittest.TestCase):
    def test_zero_one(self):
        self.assertEqual(sqrt_bin_search(0), 0)
        self.assertEqual(sqrt_bin_search(1), 1)
    def test_generic(self):
        self.assertEqual(sqrt_bin_search(11), 3)
        self.assertEqual(sqrt_bin_search(1551), 39)

if __name__ == "__main__": unittest.main()