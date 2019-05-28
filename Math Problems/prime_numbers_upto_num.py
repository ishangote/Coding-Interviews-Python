# Given a number N, find all prime numbers upto N (N included). Make sure the returned array is sorted. 
# Also known as Sieve of Eratosthenes.
"""
n = 7 => {2, 3, 5, 7}
n = 15

2   3   5   7   11  13

SoE ->
if 2 is prime all the multiples of 2 are not prime, hence remove them
0   1   2   3   4   5   6   7   8   9   10  11  12  13
2   3   4   5   6   7   8   9   10  11  12  13  14  15
^

if 3 is prime all the multiples of 3 are not prime, hence remove them
2   3   *   5   *   7   *   9   *  11  *  13  *  15
    ^

2   3   *   5   *   7   *   *   *  11  *  13  *  *
            ^

2   3   *   5   *   7   *   *   *  11  *  13  *  *
                                          ^
"""
def sieve_of_eratosthenes(n): 
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true.
    if n == 0 or n == 1: return []
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    result = []
    for p in range(2, n):
        if prime[p]: result.append(p)

    return result


import unittest
class TestSieveOfEratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes_zero_one(self):
        self.assertEqual(sieve_of_eratosthenes(0), [])
        self.assertEqual(sieve_of_eratosthenes(1), [])
    
    def test_sieve_of_eratosthenes_number(self):
        self.assertEqual(sieve_of_eratosthenes(5), [2, 3])
        self.assertEqual(sieve_of_eratosthenes(7), [2, 3, 5])
        self.assertEqual(sieve_of_eratosthenes(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(sieve_of_eratosthenes(17), [2, 3, 5, 7, 11, 13])
        self.assertEqual(sieve_of_eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if __name__ == "__main__": unittest.main()