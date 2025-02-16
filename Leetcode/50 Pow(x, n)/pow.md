# 50. Pow(x, n)

## Problem Statement

> Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x<sup>n</sup>`).

> Constraints:
>
> - -100.0 < x < 100.0
> - -2<sup>31</sup> <= n <= 2<sup>31</sup>-1
> - n is an integer.
> - Either x is not zero or n > 0.
> - -10<sup>4</sup> <= xn <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

Example 2:

```
Input: x = 2.10000, n = 3
Output: 9.26100
```

Example 3:

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

## Binary Exponentiation Solution

```

Input:
x = 2
n = 10


    2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
    -----------------
         2^5        *       2^5
        -----
    2^2 * 2^2 * 2
    ---
 2^1 * 2^1
---
base case

Output:
1024

-----------------------------------
Input:
x = 2 n = -10

n < 0 =>
res = 1 / x^n

=> x = 1/x, n = abs(n)

Output:
1/1024
```

## Approach Summary

1. If `n` is negative, transform `x` to `1/x` and make n positive.
2. Use recursion to calculate `myPow(x, n // 2)`.
3. Multiply intermediate results accordingly:

- If n is even, return `intermediate * intermediate`.
- If n is odd, return `intermediate * intermediate * x`.
