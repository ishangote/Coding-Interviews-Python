# 680. Valid Palindrome II

## Problem Statement

> Given a string s, return true if the s can be palindrome after deleting at most one character from it.

> Constraints:
>
> - 1 <= s.length <= 10<sup>5</sup>
> - s consists of lowercase English letters.

## Examples

Example 1:

```
Input: s = "aba"
Output: true
```

Example 2:

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

Example 3:

```
Input: s = "abc"
Output: false
```

## Brute Force Solution

```
Input:
s = 'abca'

s1 = 'bca'
s2 = 'aca'
s3 = 'aba'
s4 = 'abc'

* Test if palindrome can be constructed by deleting one character at a time

Output:
True
```

## Two Pointer Solution

```
Input:
s = a b d d a
    ^
            *

s =                          a b d d a
                               ^   *
                            /           \
                    a b d d a         a b d d a
                        ^ *             ^ *         => remove 'b' or remove 'd' to check if the remaining is palindrome

```
