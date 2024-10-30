# 426. Convert Binary Search Tree to Sorted Doubly Linked List

## Problem Statement

> Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
>
> You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
>
> We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)
![Output 1](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
```

![Explanation 1](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

```
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

Example 2:

```
Input: root = [2,1,3]
Output: [1,2,3]
```

## Solution

```
Input: root = None
Output: None

Input:
root = 1
           *
Output: N<-1->N
```

```
Input:
root =
        5
       /
      2
       \
        3

Output:
2 <-> 3 <-> 5
            * 5's left is the tail of the left subtree dll
            * left subtree dll's tail (3) right is 5
```

```
Input:
        5
       /
      3

        *
Output: 3 <-> 5
```

```
Input:
        2
         \
          5
        /
       3

Output: 2 <-> 3 <-> 5
        * 2's right is the head of right subtree dll
        * right subtree dll's head (3) is 2
```

```
Input:
root =
           7
        /      \
       5        15
      / \     /    \
     4   6   12     18
            /  \    /
           8   13  16

* Assume a recursive helper returns the head and tail of the DLL


   lh  lt       rh rt
   (4, 6)      (8, 18)
            7
        L /   \ R
4<->5<->6     8<->12<->13<->15<->16<->18
-       -     -                       --

node.left = lt (left tail)
lt.right = node

node.right = rh (right head)
rh.left = node

return =>
next head = lh
next tail = rt
```
