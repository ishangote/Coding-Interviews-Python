# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
# A solution will always exist. read Goldbach’s conjecture
# If there are more than one solutions possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then
# [a, b] < [c, d] 
# If a < c OR a==c AND b < d. 

"""
Example:
Input : 4
Output: 2 + 2 = 4

5 -> (2, 3)

10 -> (2, 3, 5, 7)

15 -> (2, 3, 5, 7, 11, 13)
"""
from prime_numbers_upto_num import sieve_of_eratosthenes
def prime_sum(number):
    result = set(sieve_of_eratosthenes(number))
    if len(result) == 0: return []

    for num in result:
        if (number - num) in result:
            return [num, (number - num)]

import unittest
class TestPrimeNumbersTwoSum(unittest.TestCase):
    def test_prime_sum_zero_one(self):
        self.assertEqual(prime_sum(0), [])
        self.assertEqual(prime_sum(1), [])

    def test_prime_sum_generic(self):
        self.assertEqual(prime_sum(4), [2, 2])
        self.assertEqual(prime_sum(3), [1, 2])

if __name__ == "__main__": unittest.main()