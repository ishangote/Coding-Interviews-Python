# 500. Keyboard Row

## Problem Statement

> Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
>
> In the American keyboard:
>
> - the first row consists of the characters "qwertyuiop",
> - the second row consists of the characters "asdfghjkl", and
> - the third row consists of the characters "zxcvbnm".

> Constraints:
>
> - 1 <= words.length <= 20
> - 1 <= words[i].length <= 100
> - words[i] consists of English letters (both lowercase and uppercase).

## Examples

Example 1:

```
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
```

Example 2:

```
Input: words = ["omk"]
Output: []
```

Example 3:

```
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
```

## Solution

```
first_row = {q, w,  e,  r, t, y, u, i, o, p}
second_row = {a, s,  d,  f, g, h, j, k, l}
third_row = {z, x,  c,  v, b, n, m}

Input:

words =
    *
["Hello","Alaska","Dad","Peace"]
  ^
  first char will determine which row to check for all other characters


    *
["Hello","Alaska","Dad","Peace"]
   ^
   'e' does not exist in second row => continue


            *
["Hello","Alaska","Dad","Peace"]
          ^
          lowercase 'a' is in second row

            *
["Hello","Alaska","Dad","Peace"]
           ^
          lowercase 'l' is in second row
...
```
