# 767. Reorganize String

## Problem Statement

> Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
> Return any possible rearrangement of s or return "" if not possible.

> Constraints:
>
> - 1 <= s.length <= 500
> - s consists of lowercase English letters.

## Examples

Example 1:

```
Input: s = "aab"
Output: "aba"
```

Example 2:

```
Input: s = "aaab"
Output: ""
```

## Brute Force (Backtracking) Solution

```
* Explore all possibilities

Input:
s = "aaabc"

count_map = {
    a: 3
    b: 1
    c: 1
}
res = []


res = [a]
count_map = {
    a: 2
    b: 1
    c: 1
}
prev = a


res = [a, b]
count_map = {
    a: 2
    b: 0
    c: 1
}
prev = b


res = [a, b, a]
count_map = {
    a: 1
    b: 0
    c: 1
}
prev = a


res = [a, b, a, c]
count_map = {
    a: 1
    b: 0
    c: 0
}
prev = c


res = [a, b, a, c, a]   * res complete break
count_map = {
    a: 1
    b: 0
    c: 0
}
prev = a

Output:
"abaca"
```

## Hash Map Solution

```
Input:
s = "a"
Output:
"a"

--------------------------------

Input:
s = "ab"
Output:
"ab"

--------------------------------

Input:
s = "aab"

res =
[     ]
 - - -
 ^      can fill a, b

[a    ]
 - - -
   ^      can fill only b

[a b a]
 - - -
     ^      can fill only a

Output:
"aba"

* Intuition => Most Frequent Character must be put first

--------------------------------


Input:
s = "aaabc"

char_count = {
    a: 3
    b: 1
    c: 1
}

res = []


char_count = {
    a: 3            <- most frequent
    b: 1
    c: 1
}

res = [a]


char_count = {
    a: 2
    b: 1           <- most frequent apart from res[-1] (a)
    c: 1
}

res = [a, b]


char_count = {
    a: 2            <- most frequent apart from res[-1] (c)
    b: 0
    c: 1
}

res = [a, b, a]


char_count = {
    a: 1
    b: 0
    c: 1            <- most frequent apart from res[-1] (a)
}

res = [a, b, a, c]


char_count = {
    a: 1            <- most frequent apart from res[-1] (c)
    b: 0
    c: 0
}

res = [a, b, a, c, a]


char_count = {
    a: 0
    b: 0
    c: 0
}

res = [a, b, a, c, a]
```

## Max Heap Solution

```
s = "aaabc"

max_heap = [(1, b), (1, c), (3, a)]
previous_char = None
res = []


max_heap = [(1, b), (1, c)]
max_freq_char, count =  (3, a)
previous_char = (2, a)
res = [a]


max_heap = [(1, b)]     =>   [(1, b), (2, a)]
max_freq_char, count =  (1, c)
previous_char = (2, a)  => (0, c)    * Add back previous character and reset
res = [a, c]


max_heap = [(1, b)]
max_freq_char, count =  (2, a)
previous_char = (0, c)  => (1, a) * Don't add back since count = 0
res = [a, c, a]


max_heap = []       => [(1, a)]
max_freq_char, count = (1, b)
previous_char = (1, a)  =>  (0, b)
res = [a, c, a, b]


max_heap = []
max_freq_char, count = (1, a)
previous_char = (0, b)
res = [a, c, a, b, a]
```

```
s = "aaab"

max_heap = [(1, b), (3, a)]
previous_char = None
res = []


max_heap = [(1, b)]
max_freq_char, count = (3, a)
previous_char = None    => (2, a)
res = [a]


max_heap = [(2, a)]
max_freq_char, count = (1, b)
previous_char = (2, a)  => (0, b)
res = [a, b]


max_heap = []
max_freq_char, count = (2, a)
previous_char = (0, b)  =>  (1, a)      * prev char left to process
res = [a, b, a]
```

## References

- https://leetcode.com/problems/reorganize-string/description/
- https://www.youtube.com/watch?v=2g_b1aYTHeg&ab_channel=NeetCode
