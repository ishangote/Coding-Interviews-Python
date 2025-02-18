# 249. Group Shifted Strings

## Problem Statement

> Perform the following shift operations on a string:
>
> - Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
> - Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
>
> We can keep shifting the string in both directions to form an endless shifting sequence.
>
> - For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
>
> You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

> Constraints:
>
> - 1 <= strings.length <= 200
> - 1 <= strings[i].length <= 50
> - strings[i] consists of lowercase English letters.

## Examples

Example 1:

```
Input: strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output: [["acef"],["a", "z"],["abc", "bcd", "xyz"],["az", "ba"]]
```

Example 2:

```
Input: strings = ["a"]
Output: [["a"]]
```

## Brute Force Solution

**ASCII Letters**

```
UPPER CASE LETTERS                  LOWER CASE LETTERS
A → 65                              a → 97
B → 66                              b → 98
C → 67                              c → 99
D → 68                              d → 100
E → 69                              e → 101
F → 70                              f → 102
G → 71                              g → 103
H → 72                              h → 104
I → 73                              i → 105
J → 74                              j → 106
K → 75                              k → 107
L → 76                              l → 108
M → 77                              m → 109
N → 78                              n → 110
O → 79                              o → 111
P → 80                              p → 112
Q → 81                              q → 113
R → 82                              r → 114
S → 83                              s → 115
T → 84                              t → 116
U → 85                              u → 117
V → 86                              v → 118
W → 87                              w → 119
X → 88                              x → 120
Y → 89                              y → 121
Z → 90                              z → 122
```

```
* grouped strings must have equal length
s1 = "abc"
s2 = "bcd"

* s1 and s2 can be grouped since =>
right_shift(s1) = s2
left_shift(s2) = s1


* distance between characters that are shifted remains same as the original string
s1 = "acf"                  -> distance (2, 3)
right_shift(s1) = "bdg"     -> distance (2, 3)
right_shift(s1) = "ceh"     -> distance (2, 3) * ^ all these should be grouped
...

* edge case
s1 = "acz"      -> distance (2, 23)
right_shift(s1) = "bda"     -> distance (2, -3)       * negative distance
                                                      * -3 + 26 = 23

distance = (ord(s1[idx + 1]) - ord(s1[idx]) + 26) % 26

* Utilize hashmap to store tuple of distances as keys
```

## References

- https://www.youtube.com/watch?v=g_CWHtPSQmQ&t=554s&ab_channel=CrackingFAANG
