# 143. Reorder List

## Problem Statement

> You are given the head of a singly linked-list. The list can be represented as:
>
> L0 → L1 → … → Ln - 1 → Ln
>
> Reorder the list to be on the following form:
>
> L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
>
> You may not modify the values in the list's nodes. Only nodes themselves may be changed.

> Constraints:
>
> - The number of nodes in the list is in the range [1, 5 * 10<sup>4</sup>].
> - 1 <= Node.val <= 1000

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Split-Reverse-Merge Solution

```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

1 2 3 4 5

1 2 3
4 5

1 2 3
|/|/
5 4

1. Split list at middle
2. Reverse second list
3. Merge Lists
```

Step 1: Find the Middle of the List

- Use the slow and fast pointer technique to find the middle node.
  slow moves one step at a time, while fast moves two steps at a time.
- When fast reaches the end, slow will be at the middle.

Example:

```
1 → 2 → 3 → 4 → 5
s
f

1 → 2 → 3 → 4 → 5
    s
        f

1 → 2 → 3 → 4 → 5
        s
                f

slow stops at 3 → Middle found!
```

Step 2: Reverse the Second Half

- Reverse the second half of the list in place.
- Use three pointers: prev, curr, and next to reverse the links.

Example:

```
Reverse 4 → 5 to 5 → 4:

p = None  c = s.next  s.next = None (disconnect the lists)
1 → 2 → 3    4 → 5
        s    c

1 → 2 → 3    4 ← 5
                 p   c
```

Step 3: Merge the Two Halves

```
p1   t1
1 -> 2 -> 3

5 -> 4
p2

Pseudo:
while p2:
    tmp1 = p1.next
    p1.next = p2
    p1 = tmp1
    tmp2 = p2.next
    p2.next = p1
    p2 = tmp2
```
