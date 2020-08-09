"""
Given two arrays of integers, find a pair of values (one value from each array) 
that you can swap to give the two arrays the same sum.

Input: arr1 = {4, 1, 2, 1, 1, 2}; arr2 = {3, 6, 3, 3}
Output: {1, 3}
# Swapping 1 in arr1 with 3 in arr2 will give us the same sum of 13 in both of the arrays
arr1 = {4, 3, 2, 1, 1, 2}
arr2 = {1, 6, 3, 3}


Clarifying questions:
Does the list contain negative numbers? Yes
You are not guaranteed the pair will exist. Return null in this case


Brute Force 1: O(n x m)
Iterate through the arrays and check all pairs of values. Compare new sums.

Brute Force 2: O(n x m)
Want (a, b) s.t. 
sum_A - a + b = sum_B - b + a
sum_A - sum_B = 2(a - b)
a - b = (sum_A - sum_B) // 2



Optimized1: O(nlogn + mlogm)
[4, 1, 2, 1, 2]
[6, 3, 3]
target = (sum_A - sum_B) // 2 = (10 - 12) // 2 = -1

Sort Both Arrays:
       *
[1, 1, 2, 2, 4]
[3, 3, 6]
 ^
ans = 1 - 3 = -2 therfore move *

ans = -1 == target return [2, 3]


Optimized2: Time: O(n + m) Space: O(n)
a - b = target => a = b + target

[6, 3, 3]
[4, 1, 2, 1, 2]
Use Hash Set for smaller elements:
hs = {}
target = (sum_A - sum_B) // 2 = (10 - 12) // 2 = -1

"""

def sum_swap_brute_force2(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    target = 0 if (sum_A - sum_B) % 2 != 0 else (sum_A - sum_B) // 2

    for a in A:
        for b in B:
            if a - b == target: return [a, b]

    return []

def sum_swap_optimized1(A, B):
    A = sorted(A)
    B = sorted(B)

    sum_A = sum(A)
    sum_B = sum(B)
    target = 0 if (sum_A - sum_B) % 2 != 0 else (sum_A - sum_B) // 2

    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] - B[j] == target: return [A[i], B[i]]
        
        elif A[i] - B[j] < target: i += 1
        
        else: j += 1

    return []

def sum_swap_optimized2(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    target = 0 if (sum_A - sum_B) % 2 != 0 else (sum_A - sum_B) // 2

    hs = set(A)
    for b in B:
        if b + target in hs: return [b + target, b]
    
    return []

import unittest
class TestSumSwap(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(sum_swap_brute_force2([4,1,2,1,1,2], [3,6,3,3]), [4, 6])
        self.assertEqual(sum_swap_optimized1([4,1,2,1,1,2], [3,6,3,3]), [1, 3])
        self.assertEqual(sum_swap_optimized2([4,1,2,1,1,2], [3,6,3,3]), [1, 3])

if __name__ == "__main__": unittest.main()