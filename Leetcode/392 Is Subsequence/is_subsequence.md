# 392. Is Subsequence

## Problem Statement

> Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
>
> A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
>
> Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

> Constraints:
>
> - 0 <= s.length <= 100
> - 0 <= t.length <= 10<sup>4</sup>
> - s and t consist only of lowercase English letters.

## Examples

Example 1:

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

Example 2:

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Solution

```
Input:

t = 'a'
s = 'a'     * no characters removed

Output:
True
```

```
Input:

t = 'ababcd'
     ^
s = 'bad'    * char a comes before char d in t hence it is subsequence
     *

t = a d b a b c d
    ^
s = b a d
    *

t = a d b a b c d
        ^
s = b a d
    *

t = a d b a b c d
          ^
s = b a d
      *

t = a d b a b c d
                ^
s = b a d
        *

t = a d b a b c d
                  ^
s = b a d
         * All characters parsed => return True
Output:
True
```

```
Input:

t = 'abcd'
s = 'da'    * char a comes before char d in t hence it is NOT a subsequence

t = a b c d
    ^
s = d a
    *

t = a b c d
          ^
s = d a
    *

t = a b c d
            ^  Finished parsing all characters of t => return false since s is not parsed fully
s = d a
      *

Output:
False
```

```
Input:

t = 'abcd'
s = 'axd'    * char x is not in t hence it is NOT a subsequence

t = a b c d
    ^
s = a x d
    *

t = a b c d
            ^ => return False since s is not fully parsed
s = a x d
      *

Output:
False
```
