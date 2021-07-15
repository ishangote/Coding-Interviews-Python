# Find the minimum length of the roof that covers K cars.

# You are given an List of positions of cars as to where they are parked. You are also given an integer K. 
#  The cars needs to be covered with a roof. You have to find the minimum length of roof that takes to cover K cars.
 
#  Input : 12,6,5,2      K = 3
 
#  Explanation :  There are two possible roofs that can cover K cars. One that covers the car in 2,5,6 parking spots and
#  another roof which covers 5,6,12 parking spots. The length of these two roofs are 5 and 8 respectively. Return 5
#  since that's the roof with minimum length that covers K cars.

#  Output : 5

"""
Example 1:
arr = 
[12, 6, 5, 2]
K = 3

res = 5

parking spots =>
0 1 2 3 4 5 6 7 8 9 10 11 12
    *     * *             *
    ---------
        5
          -----------------
                8

return 5

Sliding Window Approach:
arr = 
[12, 6, 5, 2]
arr.sort = 
 0  1  2  3
[2, 5, 6, 12]
 ------- L = 6 - 2 + 1 = 5
    ------- L = 12 - 5 + 1 = 8

========================================================

Example 2:
arr = [2, 5, 6, 12]
k = 5
=> return None?

========================================================


Example 3:
arr = [2, 5, 6, 12]
k = 0
=> return 0?

========================================================

Example 4:
       0  1  2  3  4
arr = [2, 5, 6, 9, 12]
       ---------- L = 9 - 2 + 1 = 8
          ---------- L = 12 - 5 + 1 = 8
k = 4

ans = 8
"""
import sys
def min_roof_length(parking_spots, k):
    # Input validations...
    # what if k > len(parking_spots)?
    if not parking_spots or k == 0: return 0
    if k > len(parking_spots): return sys.maxsize

    parking_spots.sort()
    ans = sys.maxsize
    for i in range(0, len(parking_spots) - k + 1):
        ans = min(ans, parking_spots[i + k - 1] - parking_spots[i] + 1)
    return ans

import unittest
class TestMinRoofLength(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(5, min_roof_length([12, 6, 5, 2], 3))
        self.assertEqual(8, min_roof_length([2, 5, 6, 9, 12], 4))

if __name__ == "__main__": unittest.main()