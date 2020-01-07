# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


12 -> (1 2), (12)

10 -> (10) => 1 #10 % 10 == 0
20 -> (20) => 1 #20 % 10 == 0
50 => 0 => 50 > 26 and 50 %10 == 0

01 -> (0) => 0 #leading 0

35 -> (3 5) => dp(3) * dp(5)
            => 1 * 1

226 -> (2 2 6), (22 6), (2 26)
    -> dp(2) * dp(26) + dp(22) * dp(6)
    -> 1 * 2 + 1

"""

def decode_ways(num):
    memo = {}
    return dp(num, memo)

def dp(num, memo):
    if len(num) in memo: return memo[len(num)]
    if len(num) == 1:
        if int(num) > 0: return 1
        else: return 0
    
    elif len(num) == 2:
        if int(num[0]) == 0: return 0   #leading 0
        elif int(num) <= 26:
            if int(num) % 10 == 0: return 1     #10, 20
            else: return 2      #25, 15
        else:
            if int(num) % 10 == 0: return 0     #30, 50
            else: return 1      #36. 46
            
    else:
        if int(num[0]) == 0: memo[len(num)] = 0
        elif 10 <= int(num[:2]) <= 26:
            memo[len(num)] = dp(num[1:], memo) + dp(num[2:], memo)
        else:
            memo[len(num)] = dp(num[1:], memo)
        
        return memo[len(num)]

import unittest
class TestDecodeWays(unittest.TestCase):

    def test_leading_0(self):
        self.assertEqual(decode_ways('0'), 0)
        self.assertEqual(decode_ways('03'), 0)
        self.assertEqual(decode_ways('025'), 0)
    
    def test_one_digit(self):
        self.assertEqual(decode_ways('1'), 1)
        self.assertEqual(decode_ways('5'), 1)
        self.assertEqual(decode_ways('4'), 1)

    def test_two_digit(self):
        self.assertEqual(decode_ways('12'), 2)
        self.assertEqual(decode_ways('25'), 2)
        self.assertEqual(decode_ways('21'), 2)

        self.assertEqual(decode_ways('32'), 1)
        self.assertEqual(decode_ways('54'), 1)
        self.assertEqual(decode_ways('71'), 1)

    def test_mod_10_case(self):
        self.assertEqual(decode_ways('10'), 1)
        self.assertEqual(decode_ways('20'), 1)

        self.assertEqual(decode_ways('30'), 0)
        self.assertEqual(decode_ways('500'), 0)

    def test_generic(self):
        self.assertEqual(decode_ways("226"), 3)
        self.assertEqual(decode_ways("1221"), 5)

if __name__ == "__main__": unittest.main()