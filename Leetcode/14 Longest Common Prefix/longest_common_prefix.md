# 14. Longest Common Prefix

## Problem Statement

> Write a function to find the longest common prefix string amongst an array of strings.
> If there is no common prefix, return an empty string "".

> Constraints:
>
> - 1 <= strs.length <= 200
> - 0 <= strs[i].length <= 200
> - strs[i] consists of only lowercase English letters if it is non-empty.

## Examples

Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Horizontal Scanning Solution

```
Input:
["flower", "flow", "flight"]
             ^
Init:
prefix = "flower"

Iteration
idx = 1
cur = "flow"
    does "flow" start with "flower" ? No
        does "flow" start with "flowe" ? No
            does "flow" start with "flow" ? Yes

idx = 2
cur = flight
    does "flight" start with "flow" ? No
        does "flight" start with "flo" ? No
            doe "flight" start with "fl" ? Yes


Output:
return "fl"
```
