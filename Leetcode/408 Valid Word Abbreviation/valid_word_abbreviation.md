# 408. Valid Word Abbreviation

## Problem Statement

> A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.
>
> For example, a string such as "substitution" could be abbreviated as (but not limited to):
>
> - "s10n" ("s <ins>ubstitutio</ins> n")
> - "sub4u4" ("sub <ins>stit</ins> u <ins>tion</ins>")
> - "12" ("<ins>substitution</ins>")
> - "su3i1u2on" ("su <ins>bst</ins> i <ins>t</ins> u <ins>ti</ins> on")
> - "substitution" (no substrings replaced)
>
> The following are not valid abbreviations:
>
> - "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
> - "s010n" (has leading zeros)
> - "s0ubstitution" (replaces an empty substring)
>
> Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation. A substring is a contiguous non-empty sequence of characters within a string.

> Constraints:
>
> - 1 <= word.length <= 20
> - word consists of only lowercase English letters.
> - 1 <= abbr.length <= 10
> - abbr consists of lowercase English letters and digits.
> - All the integers in abbr will fit in a 32-bit integer.

## Examples

Example 1:

```
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
```

Example 2:

```
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
```

## Two Pointer Solution

```
Input:
word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
^
abbr =
0 1 2 3 4 5
s u b 4 u 4
*


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n          => word char == abbr char
^
abbr =
0 1 2 3 4 5
s u b 4 u 4
*


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n          => word char == abbr char
  ^
abbr =
0 1 2 3 4 5
s u b 4 u 4
  *


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n          => word char == abbr char
    ^
abbr =
0 1 2 3 4 5
s u b 4 u 4
    *


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
      ^  ...  ^             => parse 4 characters in word
abbr =
0 1 2 3 4 5
s u b 4 u 4
      * *      => increment after parsing


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
              ^
abbr =
0 1 2 3 4 5
s u b 4 u 4
        *


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
                ^  ... ^
abbr =
0 1 2 3 4 5
s u b 4 u 4
          *  *


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
                         ^
abbr =
0 1 2 3 4 5
s u b 4 u 4
            *


Output: True
```

```
Input:
word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
^
abbr =
s 0 1 0 n
*


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
  ^
abbr =
s 0 1 0 n
  *           => if number starts with digit 0 => return False

Output: False
```

```
Input:
word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
^
abbr =
s 5 5 n
*


word =
0 1 2 3 4 5 6 7 8 9 10 11
s u b s t i t u t i o  n
  ^
abbr =
s 5 5 n
  ---
  *


word =
0 1 2 3 4 5 6 7 8 9 10 11 ... 56
s u b s t i t u t i o  n
                              ^           => out of range
abbr =
s 5 5 n              => not parsed fully
  ---
  *

Output: False
```

## References

- https://leetcode.com/problems/valid-word-abbreviation/
- https://www.youtube.com/watch?v=Sut-F029biM&ab_channel=CrackingFAANG
