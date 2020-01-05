# Given a list of non negative integers, arrange them such that they form the largest number.
"""
Example 1:
Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
import functools
def largest_number(arr):
    # The any() function returns True if any item in an iterable are true, otherwise it returns False. 
    # If the iterable object is empty, the any() function will return False.
    if not any(arr): return "0"
    arr = [str(x) for x in arr]
    compare = lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0) # Note: sorted in reverse order
    arr.sort(key = functools.cmp_to_key(compare))
    return ''.join(arr)

import unittest
class TestLargestNumber(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(largest_number([]), "0")
    
    def test_generic(self):
        self.assertEqual(largest_number([3, 30, 34, 5, 9]), "9534330")
    
    def test_all_zeroes(self):
        self.assertEqual(largest_number([0, 0, 0, 0]), "0")

if __name__ == "__main__": unittest.main()