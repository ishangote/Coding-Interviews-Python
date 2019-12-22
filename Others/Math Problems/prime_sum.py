# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
# A solution will always exist. read Goldbach’s conjecture
# If there are more than one solutions possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then
# [a, b] < [c, d] 
# If a < c OR a==c AND b < d. 
"""
Approach 1: SOE to get all prime numbers and then hash to find solution
Example:
Input : 4
Output: 2 + 2 = 4
10 -> (2, 3, 5, 7) -> 3, 7

Approach 2: Find prime = pair as we iterate

10

idx -> 2 to 10

2   10 - 2 = 8 not prime
3   10 - 3 = prime => return

"""
#----------------------------------------------------------
from prime_numbers_upto_num import sieve_of_eratosthenes
def prime_sum(number):
    if number % 2 != 0: return []
    result = set(sieve_of_eratosthenes(number))
    if len(result) == 0: return []

    for num in result:
        if (number - num) in result:
            return [num, (number - num)]

#----------------------------------------------------------

from verify_prime import verify_prime
def prime_sum_no_hashing(number):
    if number == 0 or number % 2 != 0: return []

    for idx in range(2, number):
        if verify_prime(idx) and verify_prime(number - idx): return [idx, number - idx]

#----------------------------------------------------------

import unittest
class TestPrimeNumbersTwoSum(unittest.TestCase):
    def test_invlaid_input(self):
        self.assertEqual(prime_sum(0), [])
        self.assertEqual(prime_sum(1), [])
        self.assertEqual(prime_sum(3), [])

        self.assertEqual(prime_sum_no_hashing(0), [])
        self.assertEqual(prime_sum_no_hashing(1), [])
        self.assertEqual(prime_sum_no_hashing(3), [])

    def test_prime_sum_generic(self):
        self.assertEqual(prime_sum(4), [2, 2])
        self.assertEqual(prime_sum(6), [3, 3])
        self.assertEqual(prime_sum(8), [3, 5])
        self.assertEqual(prime_sum(10), [3, 7])

        self.assertEqual(prime_sum_no_hashing(4), [2, 2])
        self.assertEqual(prime_sum_no_hashing(6), [3, 3])
        self.assertEqual(prime_sum_no_hashing(8), [3, 5])
        self.assertEqual(prime_sum_no_hashing(10), [3, 7])
if __name__ == "__main__": unittest.main()