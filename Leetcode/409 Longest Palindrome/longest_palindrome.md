# 409. Longest Palindrome

## Problem Statement

> Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
> Letters are case sensitive, for example, "Aa" is not considered a palindrome.

> Constraints:
>
> - 1 <= s.length <= 2000
> - s consists of lowercase and/or uppercase English letters only.

## Examples

Example 1:

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

Example 2:

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
```

## Brute Force

```
* Construct all possible strings using the characters in s
* Check which one of them are palindromes
* Return the length of the longes palindrome
```

## Solution 1

```
Input:
s = a

possible palindrome candidates => [a]

Output:
1
```

```
Input:
s = ab

possible palindrome candidates => [a, b]

Output:
1
```

```
Input:
s = aa

possible palindrome candidates => [a, aa]

Output:
2
```

```
Input:
s = aacaabbccdeee

* By definition, palindrome may have only one character without a match,
rest need to have even number of matches

char_count =
{
    a: 4    <- for even count, we can directly use it to construct the palindrome
    c: 3    <- for odd count, we can place 1 c in the middle and then use 2 c's
    b: 2    <- for even count, we can directly use it to construct the palindrome
    d: 1    <- for odd count, we can directly 1 d in the middle
    e: 3    <- for odd count, we can place 1 e in the middle and then use 2 e's
}

* Notice for odd counts, we add +1 and the remaining count can directly be used to create a palindrome
* For all odd counts, subtract it by 1 and add rest to the result
* Add 1 to the result if odd was found

Output:
11

```

## Solution 2

```
s = aacaabbccdeee
char_set = {}
res = 0

s = a a c a a b b c c d e e e
    ^
char_set = {a}
res = 0

s = a a c a a b b c c d e e e
      ^
char_set = {a}  => {} (remove from set)
res = 0 + 2 (since a already exists in set (seen once before))


s = a a c a a b b c c d e e e
        ^
char_set = {c}
res = 2

s = a a c a a b b c c d e e e
          ^
char_set = {c, a}
res = 2

s = a a c a a b b c c d e e e
            ^
char_set = {c, a} => {c}
res = 2 + 2 = 4

s = a a c a a b b c c d e e e
              ^
char_set = {c, b}
res = 4
...

* if set has some characters left, just add 1 to the res for middle char

```
