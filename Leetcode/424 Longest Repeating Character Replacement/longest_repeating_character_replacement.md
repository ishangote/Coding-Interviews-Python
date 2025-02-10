# 424. Longest Repeating Character Replacement

## Problem Statement

> You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
> Return the length of the longest substring containing the same letter you can get after performing the above operations.

> Constraints:
>
> - 1 <= s.length <= 10<sup>5</sup>
> - s consists of only uppercase English letters.
> - 0 <= k <= s.length

## Examples

Example 1:

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

Example 2:

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

## Sliding Window Solution

```
Input:
s = "ABABB"
k = 1

Question 1: Should we replace "A" or should we replace "B"?
=> We should replace the character that are less frequent to minimize replacements i.e "A"


Question 2: Should we replace "A" at index 0 or at index 2?
=> index 2 since it makes the maximum longest substring

s=
0 1 2 3 4
A B A B B
    ^

Output: 4
```

```
Input:
k = 2

s =
0 1 2 3 4 5
A B A B B A
  -------

For the above substring =>

count = {
    A: 1
    B: 3
}

Formula:
window_length - count[B] = 4 - 3 = 1
                  ^
                  most frequent character

- number of characters we need to replace to match B
- if 1 <= k => the current window is valid, i.e after k replacements we have a substring without repeating characters

Now we apply sliding window technique =>

Input:
k = 2
s =
0 1 2 3 4 5
A B A B B A
l
r

count = {
    A: 1
}

window_length - count[A] = 0 <= 2 => res = 1

k = 2
s =
0 1 2 3 4 5
A B A B B A
l
  r

count = {
    A: 1
    B: 1
}

window_length - count[A] = 1 <= 2 => res = 1


k = 2
s =
0 1 2 3 4 5
A B A B B A
l
    r

count = {
    A: 2
    B: 1
}

window_length - count[A] = 1 <= 2 => res = 3


k = 2
s =
0 1 2 3 4 5
A B A B B A
l
      r

count = {
    A: 2
    B: 2
}

window_length - count[A] = 2 <= 2 => res = 4


k = 2
s =
0 1 2 3 4 5
A B A B B A
l
        r

count = {
    A: 2
    B: 3
}

window_length - count[B] = 2 <= 2 => res = 5


k = 2
s =
0 1 2 3 4 5
A B A B B A
l
          r

count = {
    A: 3
    B: 3
}

window_length - count[B] = 3 > 2 => move left pointer


k = 2
s =
0 1 2 3 4 5
A B A B B A
  l
          r

count = {
    A: 2
    B: 3
}

window_length - count[B] = 2 <= 2 => res = 5


k = 2
s =
0 1 2 3 4 5
A B A B B A
  l
             r * (out-of-bounds => stop)

Output: 5
```
