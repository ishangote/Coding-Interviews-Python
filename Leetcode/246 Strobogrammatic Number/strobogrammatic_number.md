# 246. Strobogrammatic Number

## Problem Statement

> Given a string num which represents an integer, return true if num is a strobogrammatic number. A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

> Constraints:
>
> - 1 <= num.length <= 50
> - num consists of only digits.
> - num does not contain any leading zeros except for zero itself.

## Examples

Example 1:

```
Input: num = "69"
Output: true
```

Example 2:

```
Input: num = "88"
Output: true
```

Example 3:

```
Input: num = "962"
Output: false
```

## Solution

```
Strobogrammatic Digits:

0: 0
1: 1
2: x
3: x
4: x
5: x
6: 9
7: x
8: 8
9: 6

Example 1:

Input: num = "962"
* 180 degrees rotation => 296 != 962: return False

Output: false

Example 2:
Input:

num =
96569
^   *
    6

num =
96569
 ^ *
   9

num =
96569
  ^
  *
  Not a valid pair => False

```
