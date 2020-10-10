"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example
For n = 9, the output should be
isSumOfConsecutive2(n) = 2.
There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.
There are no ways to represent n = 8.
"""

"""
Questions:
1. Can we consider the same number multiple times for addition? 
eg 1 + 1 + 1 + 1 ...-> No

Examples:
n = 9

n = a + (a + 1) + (a + 2) + ... (a + l)
n = a(1 + 2 + 3 + 4 + .. l + 1)
a = (N- L*(L+1)/2)/(L+1)
We substitute the values of L starting from 1 till L*(L+1)/2 < N

"""
def isSumOfConsecutive2(n):
    ans = 0
    L = 1
    while L*(L+1)/2 < n:
        a = (1.0 * n - (L * (L + 1) ) / 2) / (L + 1) 
        if (a - int(a) == 0.0): 
            ans += 1
        L += 1
    return ans