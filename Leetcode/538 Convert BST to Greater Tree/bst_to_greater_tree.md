# 538. Convert BST to Greater Tree

## Problem Statement

> Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
>
> As a reminder, a binary search tree is a tree that satisfies these constraints:
>
> - The left subtree of a node contains only nodes with keys less than the node's key.
> - The right subtree of a node contains only nodes with keys greater than the node's key.
> - Both the left and right subtrees must also be binary search trees.

> Constraints:
>
> - The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
> - -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
> - All the values in the tree are unique.
> - root is guaranteed to be a valid binary search tree.

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2019/05/02/tree.png)

```
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

Example 2:

```
Input: root = [0,null,1]
Output: [1,null,1]
```

## Backward Inorder Traversal Solution

```
Input:
root =       10
           /    \
          5      20
        /  \     / \
       1    6  15  30

* Intuition: Inorder traversal of BST => sorted array

[1,  5,  6,  10, 15, 20, 30]
                         ^    <- iterate backwards accumulating sum
[87, 86, 81, 75, 65, 50, 30]   =>  res

* Traversal => right -> root -> left
* Accumulate sum and update node value

Output:
root =       75
           /    \
          86     50
        /  \     / \
       87   81  65   30
```
