# 266. Palindrome Permutation

## Problem Statement

> Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

> Constraints:
>
> - 1 <= s.length <= 5000
> - s consists of only lowercase English letters.

## Examples

Example 1:

```
Input: s = "code"
Output: false
```

Example 2:

```
Input: s = "aab"
Output: true
```

Example 3:

```
Input: s = "carerac"
Output: true
```

## Solution

```
Input:
s = "carecar"

count = {
    c: 2
    a: 2
    r: 2    * Must be divisible by 2
    e: 1    * only one character can NOT have a match
}

count = {
    c: 0
    a: 0
    r: 0
    e: 1    * Can have only 1 character with count 1
}

Output: true "carerac"

Input:
s = "ccarcarc" -> "ccarracc"

count = {
    c: 4    * Take modulo with 2 for all elements
    a: 2
    r: 2
}
=>
count = {
    c: 0
    a: 0
    r: 0
}

Output: true "carerac"
```
