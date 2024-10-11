# 507. Perfect Number

## Problem Statement

> A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
>
> Given an integer n, return true if n is a perfect number, otherwise return false.

> Constraints:
>
> - 1 <= num <= 10<sup>8</sup>

## Examples

Example 1:

```
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
```

Example 2:

```
Input: num = 7
Output: false
```

## Solution

- Algorithm to find divisors:

1. Loop through all integers from 1 to the square root of the number (let's call it n).
2. For each integer `i`, check if `n % i == 0`. If true, i is a divisor.
3. Also, if `i` is a divisor, then `n / i` is also a divisor (unless `i` equals `n / i`).
4. Return the list of divisors.
