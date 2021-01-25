
"""
Questions:
1. n < 1? return None

Examples:
getfib(1) = 0
getfib(2) = 1
getfib(3) = getfib(2) + getfib(1) = 1 + 0 = 1
getfib(4) = getfib(3) + getfib(2) = 1 + 1 = 2
...

							fib(6)
		        fib(5)			    	       fib(4)
		fib(4)         fib(3)	        fib(3)        fib(2)
 	fib(3) fib(2)   fib(2) fib(1)  fib(2)  fib(1)
 fib(2) fib(1)

For each n, we are calling 2 fibs
2 * 2 * 2 .. 2^n

Hence, time O(2^n)
"""

def nth_fibonacci_naive(n):
    if n < 1: return None
    if n == 1: return 0
    if n == 2: return 1

    return nth_fibonacci_naive(n - 1) + nth_fibonacci_naive(n - 2)