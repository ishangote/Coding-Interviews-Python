# 203. Remove Linked List Elements

## Problem Statement

> Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

> Constraints:
>
> - The number of nodes in the list is in the range [0, 104].
> - 1 <= Node.val <= 50
> - 0 <= val <= 50

## Examples

Example 1

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

Example 2:

```
Input: head = [], val = 1
Output: []
```

Example 3:

```
Input: head = [7,7,7,7], val = 7
Output: []
```

## Solution

```
Example 1:

Input:

target = 1

* Maintain dummy to fetch head later

Initialize:
        head
dummy -> 1 -> 2 -> 1 -> 1 -> 3 -> 1
 p
         c

         1
dummy ->      2 -> 1 -> 1 -> 3 -> 1
  p
              c

         1
dummy ->      2 -> 1 -> 1 -> 3 -> 1
              p
                   c

         1         1
dummy ->      2 ->   -> 1 -> 3 -> 1
              p
                        c


         1         1    1
dummy ->      2 ->   ->   -> 3 -> 1
              p
                             c

         1         1    1
dummy ->      2 ->   ->   -> 3 -> 1
                             p
                                  c

         1         1    1         1
dummy ->      2 ->   ->   -> 3 ->
                             p
                                     c


return dummy.next
Output:
    2 -> 3

```
