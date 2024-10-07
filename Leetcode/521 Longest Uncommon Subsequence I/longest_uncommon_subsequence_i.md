# 521. Longest Uncommon Subsequence I

## Problem Statement

> Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.
>
> A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
> An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.

> Constraints:
>
> - 1 <= a.length, b.length <= 100
> - a and b consist of lower-case English letters.

## Examples

Example 1:

```
Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
```

Example 2:

```
Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".
```

Example 3:

```
Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b.
Similarly, every subsequence of string b is also a subsequence of string a.
So the answer would be -1.
```

## Solution

```
* if a == b: return -1
* else return the length of larger string
```
