# 938. Range Sum of BST

## Problem Statement

> Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 2 * 10<sup>4</sup>].
> - 1 <= Node.val <= 10<sup>5</sup>
> - 1 <= low <= high <= 10<sup>5</sup>
> - All Node.val are unique.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

## Solution

```
Constraints:
1. All numbers are unique
2. It is a Binary Search Tree

lo, hi = 5, 13
root =
            10
        /         \
       4           15
      / \         /  \
     3   7      11    18
    /   / \      \
   1   6   8      12


Inorder traversal = [1, 3, 4, 6, 7, 8, 10, 11, 12, 15, 18]
                              l                 h

                           * Iterate from left to right and add to res

```

## References

- https://www.youtube.com/watch?v=uLVG45n4Sbg&ab_channel=NeetCodeIO
