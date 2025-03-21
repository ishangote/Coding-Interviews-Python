# 76. Minimum Window Substring

## Problem Statement

> Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
> The testcases will be generated such that the answer is unique.

## Examples

Example 1:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

Example 2:

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

Example 3:

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Sliding Window Solution

- Expand then Contract:

  - Expand the window until it satisfies the frequency requirement.
  - Contract (shrink) the window from the left as much as possible while it remains valid.

- Frequency Checking:

  - The helper function checks that every required character meets its frequency in the current window.
  - Although calling this helper in the inner loop can affect efficiency, it's acceptable if the character set is small.

- Guaranteed Constraints:
  - The approach works well given that the input consists only of lowercase/uppercase letters, keeping k effectively constant.
