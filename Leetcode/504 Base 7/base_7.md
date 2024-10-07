# 504. Base 7

## Problem Statement

> Given an integer num, return a string of its base 7 representation.

> Constraints:
>
> - -10<sup>7</sup> <= num <= 10<sup>7</sup>

## Examples

Example 1:

```
Input: num = 100
Output: "202"
```

Example 2:

```
Input: num = -7
Output: "-10"
```

## Solution

```
Input:
num = 100

* base 10 representation of 100:
(1 * 10 ^ 2) + (0 * 10 ^ 1) + (0 * 10 ^ 0) = 100

So the base 7 equivalent (102) can be represented as
(1 * 7 ^ 2) + (0 * 7 ^ 1) + (2 * 7 ^ 0) = 100

* To convert to base 7 we need to accumulate the remainder of the base 10 number divided by 7


100 / 7 = 14            100 % 7 = 2     ^
14 / 4  = 2             14 % 7 = 0      |   (** Read from bottom to top ** )
2 / 7 = 0               2 % 7 = 2       |


result = "202"
```
