"""
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. 
If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)

Constraints:
[time limit] 5000ms
[input] array.integer arr
1 ≤ arr.length ≤ 100
[input] integer s
[output] array.integer

----------------------------------------

[2, 7, 4, 0, 9, 5, 1, 3] target = 20
sorting...
[0, 1, 2, 3, 4, 5, 7, 9] target = 20

FIRST NESTED LOOP
 0  1  2  3  4
[0, 1, 6, 3, 5]  target = 9
 ^
       ^
    
    i     j      sm       hm
    0     1      1        {1: [(0, 1)]}
    0     2      6        ..
    0     3      3        ..
    0     4      5        {1: [(0, 1)], 6:[(0, 2)], 3:[(0, 3)], 5:[(0, 4)]}

    1     2      7         ..
    1     3      4         ..
    1     4      6

    2     3      9
    2     4      11

    3     4      8        {1: [(0, 1)], 
                           6:[(0, 2), (1, 4)], 
                           3:[(0, 3)], 
                           5:[(0, 4)], 
                           7:[(1, 2)],
                           4:[(1, 3)], 
                           9:[(2, 3)], 
                           11:[(2, 4)], 
                           8:[3, 4]}

SECOND NESTED LOOP
    i     j      sm     target(9) - sm
    0     1      1      8       => in hm => 0, 1, 3, 4 Found!
    0     2      6  
    0     3      3  
    0     4      5  

    1     2      7  
    1     3      4  
    1     4      6

    2     3      9
    2     4      11

    3     4      8

To avoid duplicates: use set
"""

from collections import defaultdict
def arr_quadruplet(arr, target):
    if len(arr) < 4: return []
    hm = defaultdict(list)
    arr = sorted(arr)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            hm[arr[i] + arr[j]].append((i, j))

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sm = arr[i] + arr[j]
            if target - sm in hm:
                k, l = hm[target - sm][0]
                hs = set([i, j, k, l])
                if len(hs) == 4: return [arr[i], arr[j], arr[k], arr[l]]
    return []

import unittest
class TestArrayQuadruplet(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(arr_quadruplet([], 20), [])
        self.assertEqual(arr_quadruplet([4, 4, 4], 12), [])

    def test_generic(self):
        self.assertEqual(arr_quadruplet([2,7,4,0,9,5,1,3], 20), [0,4,7,9])
        self.assertEqual(arr_quadruplet([4, 4, 4, 2], 16), [])
        self.assertEqual(arr_quadruplet([4, 4, 4, 4], 16), [4, 4, 4, 4])
        self.assertEqual(arr_quadruplet([1,2,3,4,5,9,19,12,12,19], 40), [4, 5, 12, 19])
        
if __name__ == "__main__": unittest.main()