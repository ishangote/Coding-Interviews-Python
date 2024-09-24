# 258. Add Digits

## Problem Statement

> Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
> Follow up: Could you do it without any loop/recursion in O(1) runtime?
>
> Constraints:
>
> - 0 <= num <= 2<sup>31</sup> - 1

## Examples

```
Example 1:

Input: num = 38
Output: 2

Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
```

Example 2:

```
Input: num = 0
Output: 0
```

## Brute Force Solution

```
Input:
num = 924
res = 0

num = 92    * 924 // 10
res = 0 + 4     * 924 % 10

num = 9
res = 4 + 2

num = 0
res = 6 + 9 = 15

---------------------

num = 15
res = 0

num = 1
res = 0 + 5

num = 0                 * stopping condition num = 0 and res is only one digit
res = 5 + 1 = 6

```

## Math Solution

```
n = 3   2   1
 ...d2  d1  d0

n = d0 * (10^0) + d1 * (10^ 1) + d2 * (10^2)...

n = d0 * [(9 * 0) + 1] + d1 * [(9 * 1) + 1] + d2 * [(9 * 11) + 1]...

n = (9 * 0) * d0 + d0 + (9 * 1) * d1 + d1 + (9 * 11) * d2 + d2...

n = d0 + d1 + d2 + [(9 * 0) * d0 + (9 * 1) * d1 + (9 * 11) * d2...]

n = d0 + d1 + d2 + [9 * (0 * d0 + 1 * d1 + 11 * d2...)]

n  =     d0 + d1 + d2 + [9 * (0 * d0 + 1 * d1 + 11 * d2...)]
%        ----------------------%----------------------------
9                              9

n % 9 = d0 + d1 + d2

Test:
n = 924
n % 9 = 6  * res

Test:
n = 81
81 % 9 = 0 * => EDGE CASE

* Divisibility Rule of 9:
* Any number where it's digits add to 9 is always divisible by 9. (18, 27, 36, 45, 54, 63, 72, 81, 90, etc.) Therefore the 'digital root' for any number divisible by 9 is always 9.
* You can see this even in larger numbers like 99 because 9 + 9 = 18, and then 1 + 8 = 9 still, so the root always becomes 9 for any numbers divisible by 9.

Test:
n = 0
0 % 9 = 0 * => EDGE CASE
```
