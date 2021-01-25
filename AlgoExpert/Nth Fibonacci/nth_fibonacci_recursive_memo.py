"""
Implementing memoization...
"""

def nth_fib_recursive_helper(n, fib):
    if n in fib: return fib[n]
    fib[n] = nth_fib_recursive_helper(n - 1, fib) + nth_fib_recursive_helper(n - 2, fib)
    return fib[n]

def nth_fib_recursive_memo(n):
    if n < 1: return None
    fib = {1: 0, 2: 1}
    return nth_fib_recursive_helper(n, fib)