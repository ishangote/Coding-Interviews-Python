# 206. Reverse Linked List

## Problem Statement

> Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Examples

Example 1:

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Example 2:

```
Input: head = [1,2]
Output: [2,1]
```

Example 3:

```
Input: head = []
Output: []
```

## Two Pointers Solution

```
Input:

N   2  ->  3  ->  5  ->  7
p   c

N  <-  2      3  ->  5  ->  7
       p      c

N  <-  2  <-  3      5  ->  7
              p      c

N  <-  2  <-  3  <-  5      7
                     p      c

N  <-  2  <-  3  <-  5  <-  7
                            p      c

return prev

Output:
7  ->  5  ->  3  ->  2

```
