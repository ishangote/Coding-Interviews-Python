"""

factors -> n % i == 0 -> i is a factor

12: {1, 2, 3, 4, 6, 12}
           ^
36: {1, 2, 3, 4, 6, 9, 12, 18, 36}
                 ^
15: {1, 3, 5, 15}

factors exist in pairs => i, n/i

a x b = n => if a < root(n) => b > root(n) else if a == b => a, b = root(n)

"""
def find_all_factors(n):
    if n == 0: return 'inf'

    result = set()
    result.add(1)
    result.add(n)
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            result.add(i)
            result.add(n / i)
    return result

import unittest
class TestAllFactors(unittest.TestCase):
    def test_all_facotrs_zero(self):
        self.assertEqual(find_all_factors(0), 'inf')
    
    def test_all_facotrs_one(self):
        self.assertEqual(find_all_factors(1), {1})

    def test_all_factors_n(self):
        self.assertEqual(find_all_factors(2), {1, 2})
        self.assertEqual(find_all_factors(3), {1, 3})
        self.assertEqual(find_all_factors(4), {1, 2, 4})
        self.assertEqual(find_all_factors(5), {1, 5})
        self.assertEqual(find_all_factors(6), {1, 2, 3, 6})
        self.assertEqual(find_all_factors(12), {1, 2, 3, 4, 6, 12})
        self.assertEqual(find_all_factors(36), {1, 2, 3, 4, 6, 9, 12, 18, 36})

if __name__ == "__main__": unittest.main()