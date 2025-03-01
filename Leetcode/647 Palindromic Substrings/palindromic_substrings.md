# 647. Palindromic Substrings

## Problem Statement

> Given a string s, return the number of palindromic substrings in it.
> A string is a palindrome when it reads the same backward as forward.
> A substring is a contiguous sequence of characters within the string.

> Constraints:
>
> 1 <= s.length <= 1000
> s consists of lowercase English letters.

## Examples

Example 1:

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

Example 2:

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
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

We need to expand for both cases and keep incrementing result for each l
```
