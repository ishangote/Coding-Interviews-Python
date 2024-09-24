# 263. Ugly Number

## Problem Statement

> An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
> Given an integer n, return true if n is an ugly number.

> Constraints:
>
> - -2<sup>31</sup> <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
```

Example 2:

```
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
```

Example 3:

```
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
```

## Solution

How to calculate prime factors of any number?

1. Start with the smallest prime number (2) and divide the number by it.
2. Check if it divides evenly. If yes, divide the number by that prime factor and continue dividing by it until it no longer divides evenly.
3. Move to the next prime number (3, 5, 7, etc.) and repeat the process.
4. Stop when the number becomes 1.

```
Example:
* Prime numbers: [2, 3, 5, 7, 11...]
* We need only [2, 3, 5]

n = 60

n = n / 2 = 30
prime_factors = [2]

n = n / 2 = 15 * Not divisible by (2)
prime_factors = [2, 2]

n = n / 3 = 5
prime_factors = [2, 2, 3]

n = n / 5   (since not divisible by 2 and 3) => STOP
prime_factors = [2, 2, 3, 5]

n = 1 * Stop
```
