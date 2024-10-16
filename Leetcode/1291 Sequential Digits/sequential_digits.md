# 1291. Sequential Digits

## Problem Statement

> An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
> Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

> Constraints:
>
> - 10 <= low <= high <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: low = 100, high = 300
Output: [123,234]
```

Example 2:

```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

## Solution 1

```
Input:
lo = 10
hi = 10

Output:
[]
```

```
Input:
lo = 10
hi = 11

Output:
[]
```

```
Input:
lo = 10
hi = 12     -> after this all numbers till 23 would not have sequential digits

Output:
[12]
```

```
Sequential digit numbers:

12
23
34
45
56
67
78
89
        * No sequential digit number can start with 9
123
234
345
456
...

1234
2345
3456
...

```

```
Input:
lo = 1000
hi = 13000

* sequential digit numbers must have between 4 and 5 digits

1 _ _ _           * first_digit = 1 => 1234

2 _ _ _           * first_digit = 2 => 2345
...

1 _ _ _ _       * first_digit = 1 => 12345
2 _ _ _ _       * first_digit = 2 => 23456
...

* How to generate 1234 => (num * 10) + (prev + 1)

num = 1
prev = 1

num = 10 + 2 = 12
prev = 2

num = 120 + (2 + 1) = 123
prev = 3

num = 123 * 10 + (3 + 1) = 1234
prev = 4
```

## Solution 2

```
* All sequential digit numbers are substrings of "123456789"

"12"
"123"
...
"2345"
"3456"
...
"123456"
...

For example:
length = 4
DIGITS =
 0 1 2 3 4 5 6 7 8
"1 2 3 4 5 6 7 8 9"
           ^
           -------


* Goal is to find all substring of number of digits
```
