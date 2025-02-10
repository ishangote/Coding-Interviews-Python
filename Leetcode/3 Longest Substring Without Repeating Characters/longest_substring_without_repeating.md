# 3. Longest Substring Without Repeating Characters

## Problem Statement

> Given a string s, find the length of the longest substring without repeating characters. A substring is a contiguous non-empty sequence of characters within a string.

> Constraints:
>
> - 0 <= s.length <= 5 \* 10<sup>4</sup>
> - s consists of English letters, digits, symbols and spaces.

## Examples

Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Brute Force Solution

```
Input:
s =
0 1 2 3 4 5 6 7
a b c a b c b b
i
      j
^  ->  check duplicates within every substring

substrings:
[a, ab, abc, abca]

Output:
3

Time: O(n^3)
Space: O(1)
```

## Sliding Window Optimization Solution

```
Input:
s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {a}
-

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {a, b}
---

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {a, b, c}
-----

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {a, b, c}
-------
^ remove a

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {b, c, a}
  -----

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {b, c, a}
  -------
  ^ remove b

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, a, b}
    -----

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, a, b}
    -------
    ^ remove c

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, a, b}
      -----

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, a, b}
      -------
      ^ remove a    * remove all chars till we find the duplicate b, then remove b
        remove b

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, b}
          ---

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {c, b}
          -----
          ^ remove c
            remove b

s =
0 1 2 3 4 5 6 7
a b c a b c b b     char_set = {b}
              -

Output:
3
```
