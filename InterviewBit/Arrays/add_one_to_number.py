"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.

Example:
If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
"""

# NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
# For example, for this problem, following are some good questions to ask :
# Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
# A : For the purpose of this question, YES
# Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
# A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

"""
[1] -> [2]
[...1]->[...2]
.
.
.
[...8]->[...9]

[0, 0, 0, 1, 2]
Remove leadign zeroes

"""


def add_one_to_number(nums):
    if not nums: return []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 9: nums[i] = 0
        else: 
            nums[i] += 1
            idx = 0
            while idx < len(nums) and nums[idx] == 0: idx += 1
            nums = nums[idx:]
            return nums

    return [1] + nums

import unittest
class TestAddOneToNumber(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(add_one_to_number([]), [])

    def test_generic_input(self):
        self.assertEqual(add_one_to_number([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(add_one_to_number([0, 9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(add_one_to_number([0, 1, 2, 3]), [1, 2, 4])

if __name__ == '__main__':unittest.main()