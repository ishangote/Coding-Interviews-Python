# 19. Remove Nth Node From End of List

## Problem Statement

> Given the `head` of a linked list, remove the nth node from the end of the list and return its head.

> Constraints:
>
> - The number of nodes in the list is sz.
> - 1 <= sz <= 30
> - 0 <= Node.val <= 100
> - 1 <= n <= sz

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

Example 2:

```
Input: head = [1], n = 1
Output: []
```

Example 3:

```
Input: head = [1,2], n = 1
Output: [1]
```

## Two Pass Solution

```
* Remove L - N + 1 element from start by finding L
```

## One Pass Solution

```
Input:
n = 2
head =
1 -> 2 -> 3 -> 4 -> 5
s
          f


head =
1 -> 2 -> 3 -> 4 -> 5
     s
               f

head =
1 -> 2 -> 3 -> 4 -> 5           (while f.next)
          s                     * Remove s.next (4)
                    f
Output:
1 -> 2 -> 3 -> 5


Input:
n = 2
head =
1 -> 2 -> 3 -> 4
s
          f

1 -> 2 -> 3 -> 4                (while f.next)
     s                          * Remove s.next (3)
               f

Output:
1 -> 2 -> 4
```
