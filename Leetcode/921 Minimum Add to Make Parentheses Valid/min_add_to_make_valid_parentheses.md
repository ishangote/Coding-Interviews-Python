# 921. Minimum Add to Make Parentheses Valid

## Problem Statement

> A parentheses string is valid if and only if:
>
> - It is the empty string,
> - It can be written as AB (A concatenated with B), where A and B are valid strings, or
> - It can be written as (A), where A is a valid string.
>
> You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
>
> - For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
>
> Return the minimum number of moves required to make s valid.

> Constraints:
>
> - 1 <= s.length <= 1000
> - s[i] is either '(' or ')'.

## Examples

Example 1:

```
Input: s = "())"
Output: 1
```

Example 2:

```
Input: s = "((("
Output: 3
```

## Solution

```
Input:
s =
0 1 2 3 4 5
( ) ) ) ( (

open_count = 0
close_count = 0

s =
0 1 2 3 4 5
( ) ) ) ( (
^
open_count = 1

s =
0 1 2 3 4 5
( ) ) ) ( (
  ^
open_count = 0

s =
0 1 2 3 4 5
( ) ) ) ( (
    ^
open_count = 0
res = 1          * no open count but encountered a closed bracket => increment result

s =
0 1 2 3 4 5
( ) ) ) ( (
      ^
open_count = 0
res = 2          * no open count but encountered a closed bracket => increment result

s =
0 1 2 3 4 5
( ) ) ) ( (
        ^
open_count = 1
res = 2          * no open count but encountered a closed bracket => increment result

s =
0 1 2 3 4 5
( ) ) ) ( (
          ^
open_count = 2
res = 2          * no open count but encountered a closed bracket => increment result

res = 2 + 2 (open_count)
```
