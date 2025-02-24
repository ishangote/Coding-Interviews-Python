# 224. Basic Calculator

## Problem Statement

> Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
>
> Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

> Constraints:
>
> - 1 <= s.length <= 3 \* 10<sup>5</sup>
> - s consists of digits, '+', '-', '(', ')', and ' '.
> - s represents a valid expression.
> - '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
> - '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
> - There will be no two consecutive operators in the input.
> - Every number and running calculation will fit in a signed 32-bit integer.

## Examples

Example 1:

```
Input: s = "1 + 1"
Output: 2
```

Example 2:

```
Input: s = " 2-1 + 2 "
Output: 3
```

Example 3:

```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Solution

Algorithm

1. Initialize variables

- `cur = 0` → Stores the current number being read.
- `sign = 1` → Tracks the sign of the current number that is being processed (+1 or -1).
- `res = 0` → Stores the running result.
- `stack = []` → Used to handle parentheses.

1. Iterate through the input string

- If digit (`0-9`) → Build the number: `cur = cur * 10 + int(ch)`.
- If `"+"` → Add `sign * cur` to `res`, reset `cur`, and set `sign = 1`.
- If `"-"` → Add `sign * cur` to `res`, reset `cur`, and set `sign = -1`.
- If `"("` → Push current `res` and sign onto the stack, reset `res`, and set sign = 1 for the new sub-expression.
- If `")"` → Add `sign * cur` to `res`, pop sign and previous `res` from the stack, and compute the updated result: `res = prev_res + prev_sign × res`
- Ignore spaces (`' '`) → Continue to the next character.

3. After iteration

- Add the last number (`sign * cur`) to `res` before returning the final result.
