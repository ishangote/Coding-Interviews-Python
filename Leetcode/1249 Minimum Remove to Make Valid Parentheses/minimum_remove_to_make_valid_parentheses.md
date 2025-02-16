# 1249. Minimum Remove to Make Valid Parentheses

## Problem Statement

> Given a string s of '(' , ')' and lowercase English characters.
>
> Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
>
> Formally, a parentheses string is valid if and only if:
>
> It is the empty string, contains only lowercase characters, or
> It can be written as AB (A concatenated with B), where A and B are valid strings, or
> It can be written as (A), where A is a valid string.

> Constraints:
>
> - 1 <= s.length <= 10<sup>5</sup>
> - s[i] is either '(' , ')', or lowercase English letter.

## Examples

Example 1:

```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

Example 2:

```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

Example 3:

```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

## Solution

```
The goal is to remove the minimum number of parentheses to make the string valid, meaning:

1. The number of opening and closing parentheses should be equal.
2. At any point in the string, the number of closing parentheses )
   should not exceed the number of opening parentheses (.

Example 1:

I:
s = "a(bc))d)"

list =
 0  1  2  3  4  5  6  7
[a, (, b, c, ), ), d, )]
    ^
balance = 1

 0  1  2  3  4  5  6  7
[a, (, b, c, ), ), d, )]
             ^
balance = 0

 0  1  2  3  4  5   6  7
[a, (, b, c, ), '', d, )]
                ^
balance = 0 * already 0, hence can remove ) at idx = 5

 0  1  2  3  4  5   6  7
[a, (, b, c, ), '', d, '']
                       ^
balance = 0 * already 0, hence can remove ) at idx = 7

Output:
"a(bc)d"

----------------------------------------------------

Example 2:
Input:
s = "(a)b(c(d)"

[(, a, ), b, (, c, (, d, )]
                         ^
balance = 1

* iterate backwards

 0  1  2  3  4  5  6  7  9
[(, a, ), b, (, c, (, d, )]
                   ^
balance = 1 * encountered "(" and balance > 0. remove idx 6

 0  1  2  3  4  5  6   7  9
[(, a, ), b, (, c, '', d, )]
balance = 0 * break

Output:
"(a)b(cd)"
```

## Quick Reference Note

Steps to make a string valid:

1. Forward Pass → Remove unmatched ) by keeping balance count.
2. Backward Pass → Remove extra ( if balance > 0.
3. Reconstruct String → Convert list back to string.

Why Remove ( from the End and Not from the Start?
When removing extra opening parentheses (, we always remove them from the end of the string, not from the start. Here's the reasoning:

1. Ensuring Minimum Removals
   If an extra ( appears earlier in the string but later gets a matching ), it becomes valid.
   Removing ( from the start prematurely might remove necessary ones that could have paired with a later ).
2. Preserving Order and Validity
   If we remove ( from the beginning instead of the end, we may break an otherwise valid structure.
   By removing from the end, we ensure that the earliest possible valid pairs remain intact.
