# 693. Binary Number with Alternating Bits

## Problem Statement

> Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

> Constraints:
>
> - 1 <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
```

Example 2:

```
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
```

Example 3:

```
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
```

## Brute Force Solution

```
1       0001

2       0010
3       0011

4       0100
5       0101
6       0110
7       0111

8       1000
9       1001
10      1010
```

```
* If two adjacent bits are the same, then the number does not have alternating bits. So, the goal is to check if every adjacent pair of bits is different.

Input:
n = 5

    0101
    0010    n >> 1
    ----    XOR
    0111            => all bits are 1

n = 6

    0110
    0011    n >> 1
    ----    XOR
    0101            => all bits are not 1

n = 10

    1010
    0101    n >> 1
    ----
    1111            => all bits are 1


* if all bits are 1, then the number + 1 will result in the next power of 2
* e.g.
        1111 + 0001 = 10000

     1111
    10000
    -----   AND
    00000   => if it is zero => True
```
