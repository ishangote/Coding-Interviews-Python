# Given a non-negative number represented as an array of digits,
# add 1 to the number ( increment the number represented by the digits ).
# The digits are stored such that the most significant digit is at the head of the list.

"""
Example:

If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]
as 123 + 1 = 124.

Constraints:
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

[0, 1, 2, 9]
          1

[9, 9, 9]
       ^
       0    carry = 1
    ^

"""

def add_one_to_number(arr):
    if not arr or len(arr) == 0: return []
    if arr[0] == 0 and len(arr) == 1: return [1]
        
    idx = 0
    while idx < len(arr) and arr[idx] == 0:
        idx += 1
    
    arr = arr[idx:]

    curr_sum = arr[-1] + 1
    carry = curr_sum // 10
    arr[-1] = curr_sum % 10

    for idx in range(len(arr) - 2, -1, -1):
        if carry == 1:
            curr_sum = arr[idx] + 1
            carry = curr_sum // 10
            arr[idx] = curr_sum % 10
        
    if carry == 1: arr.insert(0, 1)
    
    return arr

import unittest
class TestAddOneToNumber(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(add_one_to_number([]), [])

    def test_generic_input(self):
        self.assertEqual(add_one_to_number([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(add_one_to_number([0, 9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(add_one_to_number([0, 1, 2, 3]), [1, 2, 4])

if __name__ == '__main__':unittest.main()