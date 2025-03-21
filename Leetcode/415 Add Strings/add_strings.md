# 415. Add Strings

## Problem Statement

> Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
> You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

> Constraints:
>
> -
> - 1 <= num1.length, num2.length <= 10<sup>4</sup>
> - num1 and num2 consist of only digits.
> - num1 and num2 don't have any leading zeros except for the zero itself.

## Examples

Example 1:

```
Input: num1 = "11", num2 = "123"
Output: "134"
```

Example 2:

```
Input: num1 = "456", num2 = "77"
Output: "533"
```

Example 3:

```
Input: num1 = "0", num2 = "0"
Output: "0"
```

## Variation 2 (Decimal Points)

Example 1

```
Input:
num1 = "11.11"
num2 = "123.5"

Output:
"134.61"
```

Example 2

```
Input:
num1 = "9."
num2 = "9.4"

Output:
"18.4"
```

Example 3

```
Input:
num1 = ".15"
num2 = "612"

Output:
"612.15"
```

### Add Strings Variant (Decimal Points) Overview:

- **Splitting:** Divide each number into integer and fractional parts using `split('.')`.
- **Padding:**
  - **Logic Behind Padding:** To align the fractional digits correctly for addition, pad the shorter fractional part with trailing zeros. For example, when adding `"465"` and `"8"`, pad `"8"` to `"800"` so that each corresponding digit lines up. This ensures the digits are correctly summed, and any carry-over is properly handled.
  - Use `ljust` to achieve this.
- **Addition:**
  - Add the fractional parts digit-by-digit, handling any carry-over.
  - Add the integer parts, including any carry from the fractional addition.
- **Combining:** Concatenate the integer and fractional sums to form the final result.
