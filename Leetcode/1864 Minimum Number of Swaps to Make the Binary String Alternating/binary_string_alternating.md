# 1864. Minimum Number of Swaps to Make the Binary String Alternating

## Problem Statement

> Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.
>
> The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
>
> Any two characters may be swapped, even if they are not adjacent.

> Constraints:
>
> - 1 <= s.length <= 1000
> - s[i] is either '0' or '1'.

## Examples

Example 1:

```
Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
```

Example 2:

```
Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
```

Example 3:

```
Input: s = "1110"
Output: -1
```

## Solution

```
Input:
s = "110"

#1 = 2
#0 = 1

Output:
1
```

```
Input:
s = "111..0"

#1 > 2
#0 = 1

Output:
-1

Input:
s = "1111..00"

#1 > 3                  * Absolute difference between #1 and #0 should be less than / equal to 1
#0 = 2

Output:
-1
```

```
Steps:

1. Check if the transformation is possible:

- Count the number of 0s and 1s. If the absolute difference between the number of 0s and 1s is greater than 1, it's impossible to make the string alternating, and we should return -1.

2. Calculate the swaps for both patterns:

- Create two counts:
  - Mismatches where the expected position for '0' has '1'.
  - Mismatches where the expected position for '1' has '0'.
- Do this for both possible alternating patterns (one starting with 0, one starting with 1).

3. Determine the minimum number of swaps:

- For both patterns, calculate the number of swaps needed. Since each mismatch involves a misplaced 0 and a misplaced 1, the total number of swaps is half of the total mismatches.
- Return the minimum number of swaps for the two patterns.

4. Edge cases:

- A single character string is already alternating.
- Strings with equal numbers of 0s and 1s need to be handled carefully in terms of choosing the best alternating pattern.
```
