# 383. Ransom Note

## Problem Statement

> Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
>
> Each letter in magazine can only be used once in ransomNote.
>
> Constraints:
>
> - 1 <= ransomNote.length, magazine.length <= 105
> - ransomNote and magazine consist of lowercase English letters.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

## Hash Map

```
ransomNote = "aa"
magazine = "aab"

magazine_char_count = {
    a: 2
    b: 1
}

iterate over ransomNote and decrement count
```
