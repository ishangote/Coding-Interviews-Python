# 345. Reverse Vowels of a String

## Problem Statement

> Given a string s, reverse only all the vowels in the string and return it.
> The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

> - Constraints:
> -
> - 1 <= s.length <= 3 \* 10<sup>5</sup>
> - s consist of printable ASCII characters.

## Examples

Example 1:

```
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A'].
On reversing the vowels, s becomes "AceCreIm".
```

Example 2:

```
Input: s = "leetcode"
Output: "leotcede"
```

## Brute Force

```
s = IceCreAm

First pass: vowels_stack = [A, e, e, I]
Second pass: Replace vowels with stack.pop()

* Space: O(n)
```

## Two - Pointer Solution

```
s = I c e C r e A m
    ^             *

s = I c e C r e A m
    ^           *

s = A c e C r e I m
      ^       *

s = A c e C r e I m
        ^     *

s = A c e C r e I m
          ^ *

s = A c e C r e I m
          ^
          *
```
