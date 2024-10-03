# 476. Number Complement

## Problem Statement

> The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
> For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
>
> Given an integer num, return its complement.

> Constraints:
>
> 1 <= num < 2<sup>31</sup>

## Examples

Example 1:

```
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
```

Example 2:

```
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

## Solution

```
* How to flip bits?
* XOR operator

bit      1/0
1   xor   1     => 0    (flip 1 bit to 0)
0   xor   0     => 0

1   xor   0     => 1
0   xor   1     => 1    (flip 0 bit to 1)


Input:
n = 5

        1 0 1 (5)
        1 1 1 (7)    * bit mask => How to find this? => (2 ^ number of bits) - 1 => (2 ^ 3) - 1
    xor -------
        0 1 0

Output:
010 => 2


Input:
n = 9
        1 0 0 1 (9)
        1 1 1 1 (15)    * bit mask => How to find this? => 2 ^ 4 - 1
    xor -------
        0 1 1 0 (6)

Output:
7

* How to find the number of bits?
    - Maintain count and right shift until 0

n = 1 0 1
count = 0

n = 0 1 0
count = 1

n = 0 0 1
count = 2

n = 0 0 0
count = 3
```
