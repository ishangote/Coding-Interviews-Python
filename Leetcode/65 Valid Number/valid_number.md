# 65. Valid Number

## Problem Statement

> Given a string s, return whether s is a valid number.
>
> For example, all the following are valid numbers: `"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"`, while the following are NOT valid numbers: `"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"`.
>
> Formally, a valid number is defined using one of the following definitions:
>
> - An integer number followed by an optional exponent.
> - A decimal number followed by an optional exponent.
> - An integer number is defined with an optional sign '-' or '+' followed by digits.
>
> A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
>
> - Digits followed by a dot '.'.
> - Digits followed by a dot '.' followed by digits.
> - A dot '.' followed by digits.
>
> An exponent is defined with an exponent notation `e` or `E` followed by an integer number.
>
> The digits are defined as one or more digits.

> Constraints:
>
> - 1 <= s.length <= 20
> - s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

## Examples

Example 1:

```
Input: s = "0"
Output: true
```

Example 2:

```
Input: s = "e"
Output: false
```

Example 3:

```
Input: s = "."
Output: false
```

## Solution

#### ✅ Valid Numbers

1. Basic integers

- `123` (positive integer)
- `+123` (positive integer with sign)
- `-123` (negative integer)
- `0` (zero)

2. Floating-point numbers

- `3.14` (decimal number)
- `-3.14` (negative decimal)
- `+3.14` (positive decimal)
- `0.5` (leading zero before decimal)
- `.5` (decimal without leading zero)
- `5.` (decimal without trailing digits)

3. Scientific notation (exponential format)

- `2e10` (integer exponent)
- `-2E10` (negative number with exponent)
- `3.14e2` (decimal with exponent)
- `1e-3` (negative exponent)
- `5E+3` (positive exponent)

#### ❌ Invalid Numbers

1. Alphabetic characters

- `abc` (completely invalid input)
- `3a14` (digits mixed with letters)
- `3e1.2` (e must be followed by an integer)

2. Multiple decimal points

- `3.14.15` (two decimal points)

3. Exponent errors

- `e3` (e without leading digits)
- `3e` (e without following digits)
- `3e+` (e followed by just +, missing number)
- `3e-` (e followed by just -, missing number)

3. Sign misplacement

- `+-3` (multiple signs before number)
- `3e+1.5` (e must be followed by an integer, not a decimal)
- `3.1.4e2` (multiple decimal points)

4. Empty or only sign characters

- `''` (empty string)
- `+` (sign without number)
- `-` (sign without number)

#### Intrinsic String Methods

1. `isdigit()`: Returns True if all characters are digits. (Works only for positive numbers)
2. `isalpha()`: Returns True if all characters are alphabetic (letters only).

## References

- https://www.youtube.com/watch?v=5c6MdetEfoA&ab_channel=CrackingFAANG
