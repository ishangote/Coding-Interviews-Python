# 459. Repeated Substring Pattern

## Problem Statement

> Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

> Constraints:
>
> - 1 <= s.length <= 10<sup>4</sup>
> - s consists of lowercase English letters.

## Examples

Example 1:

```
Input: s = "abab"
Output: True
Explanation: It is the substring "ab" twice.
```

Example 2:

```
Input: s = "aba"
Output: False
```

Example 3:

```
Input: s = "abcabcabcabc"
Output: True
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```

## Brute Force Solution

```
Input:
s = "a"

Output:
False
```

```
Input:
s = "ab"

Output:
False
```

```
Input:
s = "ababab"

s length = 6

* possible substrings can only have length which can be divided evenly by length of s
* possible substring can not have the same length as s

length of substrings =   1    2      3      4        5        6
substrings           = ["a", "ab", "aba", "abab", "ababa", "ababab"]
                              ^      ^
                             (possible)

len = 6

    0 1 2 3 4 5
s = a b a b a b         * len % (j + 1 - i) != 0
    i
    j

possible = []


    0 1 2 3 4 5
s = a b a b a b         * len % (j + 1 - i) == 0
    i
      j

possible = [ab]


    0 1 2 3 4 5
s = a b a b a b         * len % (j + 1 - i) == 0
    i
        j

possible = [ab, aba]


    0 1 2 3 4 5
s = a b a b a b         * len % (j + 1 - i) != 0
    i
          j

possible = [ab, aba]


    0 1 2 3 4 5
s = a b a b a b         * len % (j + 1 - i) != 0
    i
            j

possible = [ab, aba]



    0 1 2 3 4 5
s = a b a b a b         * (j + 1 - i) == len
    i
              j

possible = [ab, aba]

* Notice that i does not need to increment since all possible substrings must start with s[0]

* Iterate over possible and check if substring * (len / len(substring)) == s
* ab * (6 / 2) = ab * 3 = ababab == s

Output:
True
```

## Optimized Solution

- if the string has a repeating pattern, it should appear if the string is concatenated with itself
- if a string is composed of a repeated substring, then doubling the string and excluding the first and last characters should still contain the original string somewhere in between

```
Input:
input_string = "abab"

* double of input string =>
abababab

* remove first and last characters
bababa

* abab is still part of the string

Output:
True
```

```
Input:
input_string = "ababa"

* double of input_string =>
ababaababa

* remove first and last characters =>
babaabab

* ababa is not part of the string anymore

Output:
False
```
