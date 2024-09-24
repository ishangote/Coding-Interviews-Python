# 231. Power of Two

## Problem Statement

> Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2<sup>x</sup>.
>
> Follow up: Could you solve it without loops/recursion?

> Constraints:
>
> - -2<sup>31</sup> <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 1
Output: true
Explanation: 20 = 1
```

Example 2:

```
Input: n = 16
Output: true
Explanation: 24 = 16
```

Example 3:

```
Input: n = 3
Output: false
```

## Brute Force

```
Input:
n = 16

* If n % 2 != 0: return False
* n = n // 2
* n == 1: return True
```

## Bit Manipulation

```
1     0001
2     0010
4     0100
8     1000
16   10000

  10000
& 01111 <- Inverse
  -----
  00000

* All bits have a single 1 bit
* Inverse of a binary number having only single 1 bit can be calculated by subtracting 1 from it
* AND inverse of the number and number. If it is zero, then it is power of two
```
