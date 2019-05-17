# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
# [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

-123 => -321

"""

def reverse_integer(x):
    pos_x = abs(x)
    result = 0

    while pos_x:
        result *= 10
        result += pos_x % 10
        pos_x //= 10

    if result > 2147483648: return 0
    return result if x >= 0 else -1 * result

import unittest
class TestReverseInteger(unittest.TestCase):
    def test_x_0(self):
        self.assertEqual(reverse_integer(0), 0)

    def test_rev_x_exceed(self):
        self.assertEqual(reverse_integer(-1322421341234213421321), 0)

    def test_pos_neg_result(self):
        self.assertEqual(reverse_integer(123), 321)
        self.assertEqual(reverse_integer(-123), -321)

if __name__ == "__main__": unittest.main()