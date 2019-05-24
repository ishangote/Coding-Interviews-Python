
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
    if not a or not b: return a or b
    
    idxa, idxb = len(a) - 1, len(b) - 1
    ans = ""
    carry = 0

    while idxa >= 0 or idxb >= 0 or carry:
        temp_a = temp_b = sum = 0
        if idxa >= 0:
            temp_a = int(a[idxa])
            idxa -= 1
        
        if idxb >= 0:
            temp_b = int(b[idxb])
            idxb -= 1

        sum = temp_a ^ temp_b ^ carry
        ans += str(sum)
        carry = (temp_a & temp_b) | (carry & (temp_a ^ temp_b))

    return a[::-1]

import unittest
class TestFullAdderBinary(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(add_binary("", '1'), '1')
        self.assertEqual(add_binary("101", ""), "101")

    def test_generic(self):
        self.assertEqual(add_binary("1010", "1011"), "10101")

if __name__ == "__main__": unittest.main()