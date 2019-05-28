# Given a number N, verify if N is prime or not. Return True if N is prime, else return False.

"""
prime number -> positive num divided only by 1 and n

n factors
1 {1}       -> not prime
2 {1, 2}    -> prime
3 {1, 3}    -> prime
4 {1, 2, 4} -> not prime
5 {1, 5}    -> not prime

i -> 2 -> n - 1 => if n % i == 0: not prime
optimization =>
i -> 2 -> root(n) => if n % i == 0: not prime
"""
def verify_prime(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

import unittest
class TestVerifyPrimeNumber(unittest.TestCase):
    def test_verify_prime_zero_one(self):
        self.assertEqual(verify_prime(0), False)
        self.assertEqual(verify_prime(1), False)

    def test_verify_prime_number(self):
        self.assertEqual(verify_prime(2), True)
        self.assertEqual(verify_prime(3), True)
        self.assertEqual(verify_prime(5), True)
        self.assertEqual(verify_prime(7), True)
        self.assertEqual(verify_prime(11), True)
        self.assertEqual(verify_prime(13), True)

    def test_verify_not_prime_number(self):
        self.assertEqual(verify_prime(4), False)
        self.assertEqual(verify_prime(6), False)
        self.assertEqual(verify_prime(8), False)
        self.assertEqual(verify_prime(9), False)
        self.assertEqual(verify_prime(10), False)
        self.assertEqual(verify_prime(12), False)
        self.assertEqual(verify_prime(14), False)
        self.assertEqual(verify_prime(15), False)

if __name__ == "__main__":unittest.main()