
# Given two binary strings, return their sum (also a binary string). The input strings are both non-empty and contains only characters 1 or 0.
"""
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


a   b   cin     cout    sum
0   0   0       0       0
0   0   1       0       1
0   1   0       0       1
0   1   1       1       0
1   0   0       0       1
1   0   1       1       0
1   1   0       1       0
1   1   1       1       1


sum = a XOR b XOR cin
cout = (a & b) or (cin & (a XOR b))

"""

def add_binary(a, b):
    if not a and not b: return "0"
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    ans = ""

    while i >=0 or j >= 0 or carry:
        temp_a = temp_b = s = 0

        if i >= 0:
            temp_a = int(a[i])
            i -= 1

        if j >= 0:
            temp_b = int(b[j])
            j -= 1

        s = temp_a ^ temp_b ^ carry
        carry = (temp_a & temp_b) | (carry & (temp_a ^ temp_b))
        ans += str(s)

    return ans[::-1]

import unittest
class TestFullAdderBinary(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(add_binary("", '1'), '1')
        self.assertEqual(add_binary("101", ""), "101")
        self.assertEqual(add_binary("", ""), "0")
        
    def test_generic(self):
        self.assertEqual(add_binary("1010", "1011"), "10101")
        self.assertEqual(add_binary("11", "1"), "100")

if __name__ == "__main__": unittest.main()