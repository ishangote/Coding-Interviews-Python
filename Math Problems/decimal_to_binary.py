"""
        n//2         n%2
n       quotient     remainder
125     62           1
62      31           0
31      15           1
15      7            1
7       3            1
3       1            1
1       0            1      

"""
def decimal_to_binary(number):

    if number == 0: return '0'
    result = ''
    while number > 0:
        remainder = number % 2
        result += str(remainder)
        number = number // 2
    
    return result[::-1]

import unittest
class TestDecimalToBinary(unittest.TestCase):
    def test_zero_to_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_one_to_one(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(125), '1111101')
        self.assertEqual(decimal_to_binary(135), '10000111')
        self.assertEqual(decimal_to_binary(27), '11011')
        self.assertEqual(decimal_to_binary(17), '10001')

if __name__ == "__main__":unittest.main()