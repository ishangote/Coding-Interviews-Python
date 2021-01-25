import unittest
from nth_fibonacci_naive_recursive import nth_fibonacci_naive
from nth_fibonacci_recursive_memo import nth_fib_recursive_memo
from nth_fibonacci_iterative_memo import nth_fibonacci_iterative_memo


class TestNthFibonacci(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(nth_fibonacci_naive(0), None)
        self.assertEqual(nth_fib_recursive_memo(0), None)
        self.assertEqual(nth_fibonacci_iterative_memo(0), None)

    def test_generic(self):
        self.assertEqual(nth_fibonacci_naive(6), 5)
        self.assertEqual(nth_fib_recursive_memo(6), 5)
        self.assertEqual(nth_fibonacci_iterative_memo(6), 5)

if __name__ == "__main__": unittest.main()