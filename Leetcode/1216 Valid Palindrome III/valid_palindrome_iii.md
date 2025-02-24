# 1216. Valid Palindrome III

## Problem Statement

> Given a string `s` and an integer `k`, return true if `s` is a `k-palindrome`.
> A string is `k-palindrome` if it can be transformed into a palindrome by removing at most k characters from it.

> Constraints:
>
> - 1 <= s.length <= 1000
> - s consists of only lowercase English letters.
> - 1 <= k <= s.length

## Examples

Example 1:

```
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
```

Example 2:

```
Input: s = "abbababa", k = 1
Output: true
```

## Top-Down With Memoization Solution

```
k = 2
input_string =                                          0 1 2 3 4 5 6     l  h  k
                                                       "a b x d y b a"   (0, 6, 2)
                                                          ^       *
                                                        0 1 2 3 4 5 6    (2, 4, 2)
                                                       "a b x d y b a"
                                                            ^   *
                                                /                         \
                                  0 1 2 3 4 5 6                              0 1 2 3 4 5 6
                       (2, 3, 1) "a b x d y b a"                            "a b x d y b a" (3, 4, 1)
                                      ^ *                                          ^ ^
                                /           \                                   /                       \
                  0 1 2 3 4 5 6            0 1 2 3 4 5 6                    0 1 2 3 4 5 6                0 1 2 3 4 5 6
       (2, 2, 0) "a b x d y b a"          "a b x d y b a" (3, 3, 0)        "a b x d y b a" (3, 3, 0)    "a b x d y b a" (4, 4, 0)
                      ^                          ^        ---------               ^         ---------            ^
                      *                          *                                *                              *


(3, 3, 0) => indicates repeated work * memoization
```
