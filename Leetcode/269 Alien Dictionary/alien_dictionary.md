# 269. Alien Dictionary

## Problem Statement

> There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
>
> You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are sorted lexicographically by the rules of this new language.
>
> If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return `""`.
>
> Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

> Constraints:
>
> - 1 <= words.length <= 100
> - 1 <= words[i].length <= 100
> - words[i] consists of only lowercase English letters.

## Examples

Example 1:

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

Example 2:

```
Input: words = ["z","x"]
Output: "zx"
```

Example 3:

```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## Topological Sort Solution

```
Input:
words = ["wrt", "wrf", "er", "ett", "rftt"]

lexicographically sorted => wrt < wrf < er < ett < rftt

word 1: wrf
          |       => f -> t
word 2: wrt

Similarly,


word 1: wrf
        |         => w -> e
word 2: er


word 1: er
         |        => r -> t
word 2: ett


word 1: ett
        |         => e -> r
word 2: rftt

Note, once order is found between pairs, we DO NOT increment both pointers.
```
