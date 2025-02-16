# 543. Diameter of Binary Tree

## Problem Statement

> Given the root of a binary tree, return the length of the diameter of the tree.
>
> The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
>
> The length of a path between two nodes is represented by the number of edges between them.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
> - -100 <= Node.val <= 100

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

Example 2:

```
Input: root = [1,2]
Output: 1
```

## DFS Solution

```
Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

    1 -> 0

    1
   2   -> 1

    1    -> 2
  2   3

    1    -> 3   => left_height = 2 right_height = 1
  2   3
4

         1    -> 5 => left_height = 2 right_height = 3
     2      3
   4   5       6
            7

ans = left_height + right_height
```
