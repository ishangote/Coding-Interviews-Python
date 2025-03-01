# 5. Longest Palindromic Substring

## Problem Statement

> Given a string s, return the longest palindromic substring in s. A substring is a contiguous non-empty sequence of characters within a string.

> Constraints:
>
> 1 <= s.length <= 1000
> s consist of only digits and English letters.

## Examples

Example 1:

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

Example 2:

```
Input: s = "cbbd"
Output: "bb"
```

## Expand Around Center Solution

```
Consider a possible substring in a large string =>
CASE 1
    0  1  2
    a  b  a
     <-l
       r->
    center (odd case)           * expand around idx


CASE 2
s = 0  1  2  3
    a  b  b  a
     <-l
          r->
    center (even case)          * expand around idx, idx + 1

We need to expand for both cases, and check for maximum length substring
```

## References

- https://www.youtube.com/watch?v=V-sEwsca1ak&t=190s&ab_channel=TusharRoy-CodingMadeSimple
