#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
#which has the largest product.
"""
prev_max_prod = -1
prev_min_prod = -1

[-1, 6, 2, 3]
  ^
prev_max_prod = -1
prev_min_prod = -1

[-1, 6, -2, 3]
         ^ 
prev_max_prod = 12
prev_min_prod = -6

[-1, 6, -2, 3]
            ^ 
prev_max_prod = 18
prev_min_prod = -6

"""

def max_subarr_product(arr):
    if len(arr) == 0: return arr    #edge case -> no num in arr
    prev_max_prod, prev_min_prod, result = arr[0], arr[0], arr[0]

    for num in arr[1:len(arr)]:     #edge case -> only one num in arr
        curr_max_product = max(prev_max_prod * num, prev_min_prod * num, num)
        curr_min_product = min(prev_max_prod * num, prev_min_prod * num, num)

        result = max(result, curr_max_product)

        prev_max_prod = curr_max_product
        prev_min_prod = curr_min_product

    return result

#------------------------------------
# Testing...

import unittest
class TestMaxSubarrProduct(unittest.TestCase):
    def test_none_arr(self):
        self.assertEqual(max_subarr_product([]), [])
        self.assertEqual(max_subarr_product([-1]), -1)

    def test_all_negative_even_len(self):
        self.assertEqual(max_subarr_product([-2, -1, -3, -4]), 24)
    
    def test_all_negative_odd_len(self):
        self.assertEqual(max_subarr_product([-2, -1, -3]), 3)
    
    def test_elem_0(self):
        self.assertEqual(max_subarr_product([-2,0,-1]), 0)
        self.assertEqual(max_subarr_product([0, -2, 3, -2]), 12)
        
    def test_max_subarr_product(self):
        self.assertEqual(max_subarr_product([2,3,-2,4]), 6)
        self.assertEqual(max_subarr_product([1, 6, -2, 3]), 6)
        self.assertEqual(max_subarr_product([-1, -6, 2, -3]), 36)

if __name__ == "__main__": unittest.main()