# 20. Valid Parentheses

## Problem Statement

> Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
>
> An input string is valid if:
>
> 1. Open brackets must be closed by the same type of brackets.
> 2. Open brackets must be closed in the correct order.
> 3. Every close bracket has a corresponding open bracket of the same type.

## Examples

Example 1:

```
Input: s = "()"
Output: true
```

Example 2:

```
Input: s = "()[]{}"
Output: true
```

Example 3:

```
Input: s = "(]"
Output: false
```

Example 4:

```
Input: s = "([])"
Output: true
```

## Solution

```
Examples:

Input: ")"
Output:False -> If string starts with closing parentheses, return false


Input: "("
Output: False
-> If a opening parentheses does not have corresponding closing parentheses, return false


Input:

0 1 2 3 4 5
( { [ ] } )
      ^

stack = ["(", "{",  "["]

- if current is opening parentheses, append to stack
-> else if current is closing parentheses,
    - check if top of the stack has corresponding opening parentheses
    - if yes, then pop, if no then return False

```
