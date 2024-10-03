# 405. Convert a Number to Hexadecimal

## Problem Statement

> Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used. All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
>
> Note: You are not allowed to use any built-in library method to directly solve this problem.

> Constraints:
>
> - -2<sup>31</sup> <= num <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: num = 26
Output: "1a"
```

Example 2:

```
Input: num = -1
Output: "ffffffff"
```

## Solution

```
* Hexadecimal Number: base 16

0 - 0
1 - 1
2 - 2
3 - 3
4 - 4
5 - 5
6 - 6
7 - 7
8 - 8
9 - 9
10 - A
11 - B
12 - C
13 - D
14 - E
15 - F
```

```
* Algorithm:

if num = 0: return "0"
if num < 0: num = two's compliment of num

while num > 0:
    remainder = num % 16
    res <- remainder(hex equivalent)

return reversed res
```
