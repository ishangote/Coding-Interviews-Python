"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Approach 1:

Approach 2: n = 200 Excellent Solution!

200 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 => Cyclic!!!
                                                 s
                                                 f
                                                 s = f != 1 => not happy
                         .....
                         |   |
                         *
19 -> 82 -> 68 -> 100 -> 1 ...
                         s
                         f

                        s = f = 1 => happy number
"""

def sum_square_digits(num):
    sum = 0
    while num != 0:
        sum += (num % 10) * (num % 10)
        num //= 10
    return sum

def is_happy(n):
    slow_pointer, fast_pointer = n, sum_square_digits(sum_square_digits(n))
    while fast_pointer != slow_pointer:
        fast_pointer = sum_square_digits(fast_pointer)
        fast_pointer = sum_square_digits(fast_pointer)
        slow_pointer = sum_square_digits(slow_pointer)

    return True if slow_pointer == 1 else False

import unittest
class TestHappyNumber(unittest.TestCase):

    def test_0(self):
        self.assertEqual(is_happy(0), False)
        self.assertEqual(is_happy(1), True)

    def test_not_happy_number(self):
        self.assertEqual(is_happy(5), False)
        self.assertEqual(is_happy(8), False)
        self.assertEqual(is_happy(21), False)
        self.assertEqual(is_happy(85), False)
        self.assertEqual(is_happy(108), False)
        self.assertEqual(is_happy(200), False)
        self.assertEqual(is_happy(221), False)
        
    def test_happy_numbers(self):
        self.assertEqual(is_happy(19), True)
        self.assertEqual(is_happy(23), True)
        self.assertEqual(is_happy(28), True)
        self.assertEqual(is_happy(31), True)
        self.assertEqual(is_happy(44), True)
        self.assertEqual(is_happy(49), True)
        self.assertEqual(is_happy(68), True)
        self.assertEqual(is_happy(133), True)
        self.assertEqual(is_happy(139), True)

if __name__ == "__main__": unittest.main()