# Your are given an array of positive integers nums. Print the number of (contiguous) subarrays 
# where the product of all the elements in the subarray is less than k.
"""
Sliding Window =>

count += e - s + 1

[10, 2, 5, 6]   k = 100
 ^
 s = 0
 e = 0
 p = 10 < 100
 count = 1

[10, 2, 5, 6]   k = 100
     ^
 s = 0
 e = 1
 p = 20 < 100
 count = 3

 [10, 2, 5, 6]   k = 100
      ^  ^
 s = 1
 e = 2
 p = 100 == 100 => s++ => p / arr[s] = 100/10 = 10
 count = 5

 [10, 2, 5, 6]   k = 100
      ^     ^
 s = 1
 e = 3
 p = 60 < 100
 count = 8
"""

def subarr_product(arr, k):
    if len(arr) == 0: return 0
    
    count, s, max_prod = 0, 0, 1

    for e in range(len(arr)):
        max_prod *= arr[e]

        while max_prod >= k and s < e:
            max_prod /= arr[s]
            s += 1

        if max_prod < k:
            count += (e - s + 1)

    return count

import unittest
class TestSubarrProdLTK(unittest.TestCase):
    def test_null_arr(self):
        self.assertEqual(subarr_product([], 100), 0)

    def test_len_1_arr(self):
        self.assertEqual(subarr_product([12], 15), 1)
        self.assertEqual(subarr_product([12], 10), 0)

    def test_k_0_input(self):
        self.assertEqual(subarr_product([1, 2, 3, 4], 0), 0)

    def test_subarr_prod_ltk(self):
        self.assertEqual(subarr_product([1, 2, 3, 4], 10), 7)
        self.assertEqual(subarr_product([10, 5, 2, 6], 100), 8)

if __name__ == "__main__": unittest.main()