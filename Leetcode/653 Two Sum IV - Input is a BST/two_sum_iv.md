# 653. Two Sum IV - Input is a BST

## Problem Statement

> Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

## Solution

```
* In-order traversal of BST is a sorted array

Input:
target = 12
root =
            5
          /   \
         3     6
        / \     \
       2   4     7


inorder = [2, 3, 4, 5, 6, 7]
           l              r     sum = 9 < target

inorder = [2, 3, 4, 5, 6, 7]
              l           r     sum = 10 < target

inorder = [2, 3, 4, 5, 6, 7]
                 l        r     sum = 11 < target

inorder = [2, 3, 4, 5, 6, 7]
                    l     r     sum = 12 == target
```
