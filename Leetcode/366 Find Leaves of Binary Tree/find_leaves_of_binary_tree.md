# 366. Find Leaves of Binary Tree

## Problem Statement

> Given the root of a binary tree, collect a tree's nodes as if you were doing this:
>
> - Collect all the leaf nodes.
> - Remove all the leaf nodes.
> - Repeat until the tree is empty.

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 100].
> - -100 <= Node.val <= 100

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/16/remleaves-tree.jpg)

```
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
```

Example 2:

```
Input: root = [1]
Output: [[1]]
```

## Simulation Solution

```
Input:
root = 1

Output: [[1]]
```

```
Input:
root =
        1
       / \
      2   3 * leaf
     / \
    4   5   * leaf
    * leaf

cur = [4, 5, 3]
res = [[4, 5, 3]]

         1
        / \
leaf * 2   N    * Once we visit leaf nodes we must update parent's left/right to None
      / \
     N   N

cur = [2]
res = [[4, 5, 3], [2]]


         1 * leaf
        / \             * Once we visit leaf nodes we must update parent's left/right to None
       N   N

cur = [1]
res = [[4, 5, 3], [2], [1]]

Output: [[4, 5, 3], [2], [1]]
```
