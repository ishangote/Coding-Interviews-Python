"""
Given integers n, k return number of substrings of str(n) of size k are divisible by n (n % substr(n) == 0)
1 <= n


"""
def substring_divisor(int_num, k):
    ans = 0
    n = str(int_num)
    visited = set()
    for i in range(len(n)):
        for j in range(i + 1, len(n) + 1):
            tmp = n[i : j]
            if len(tmp) == k and tmp not in visited and int_num % int(tmp) == 0: ans += 1
    return ans

import unittest
class TestSubstringDivisor(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(substring_divisor(120, 2), 2)

if __name__ == "__main__": unittest.main()