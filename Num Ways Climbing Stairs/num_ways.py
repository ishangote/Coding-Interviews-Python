#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Note: Given n will be a positive integer.

"""

n = 4

n1 = 1 (1)
n2 = 2 (12, 2)
n3 = 3 (13, 123, 23)
n4 = 5 (124, 23, 134, 1234, 234)
n5 = 8 (...)

fibonacci series...

fib(n) = fib(n-1) + fib(n-2)

"""
import unittest
def num_ways(n):
    if n == 1: return 1
    if n == 0: return 1 

    fib1 = 1
    fib2 = 2

    for i in range(3, n + 1):
        fib_next = fib1 + fib2
        fib1 = fib2
        fib2 = fib_next

    return fib2

class TestNumWaysToClimbNStairs(unittest.TestCase):
    def test_no_stairs(self):
        self.assertEqual(num_ways(0), 1)

    def test_one_step(self):
        self.assertEqual(num_ways(1), 1)
    
    def test_num_ways(self):
        self.assertEqual(num_ways(3), 3)
        self.assertEqual(num_ways(4), 5)
        self.assertEqual(num_ways(5), 8)

if __name__ == "__main__":unittest.main()