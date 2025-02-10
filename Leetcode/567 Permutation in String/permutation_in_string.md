# 567. Permutation in String

## Problem Statement

> Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise. A permutation is a rearrangement of all the characters of a string.
> In other words, return true if one of s1's permutations is the substring of s2.

> Constraints:
>
> - 1 <= s1.length, s2.length <= 10<sup>4</sup>
> - s1 and s2 consist of lowercase English letters.

## Examples

Example 1:

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

Example 2:

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Sliding Window Solution

```
Input:
s1 = "abc"
s2 = "xyadcbamn"

=> we need to find a window of length of s1 in s2 which has exact same characters of s1

s1 = "abc"
s2 =
0 1 2 3 4 5 6 7 8
x y a d c b a m n
-----
l   h
            0  1  2  3 ...
s1_count = [1, 1, 1, 0 ...]     * 26 characters
s2_count = [1, 0, 0, 0 ...]     * 26 characters

* For each window check if s1_count == s2_count: return True

Output: True
```
