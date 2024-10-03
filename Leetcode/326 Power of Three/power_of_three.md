# 326. Power of Three

## Problem Statement

> Given an integer n, return true if it is a power of three. Otherwise, return false. An integer n is a power of three, if there exists an integer x such that n == 3<sup>x</sup>.

## Examples

Example 1:

```
Input: n = 27
Output: true
Explanation: 27 = 3^3
```

Example 2:

```
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.
```

Example 3:

```
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).
```

## Brute Force Solution

```
* Pseudo Code *

while number % 3 == 0:
    num = num // 3

return num == 1
```
