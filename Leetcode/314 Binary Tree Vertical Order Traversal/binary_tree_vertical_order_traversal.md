# 314. Binary Tree Vertical Order Traversal

> If multiple nodes are in the same row and column, they should be ordered from left to right.

## Problem Statement

> Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
>
> If two nodes are in the same row and column, the order should be from left to right.

> Constraints:
>
> - The number of nodes in the tree is in the range [0, 100].
> - -100 <= Node.val <= 100

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/09/23/image1.png)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/09/23/image3.png)

```
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
```

Example 3:

![Example 1](https://assets.leetcode.com/uploads/2024/09/23/image2.png)

```
Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
```

## Level - Order + Hash-Map + Sort Keys Solution

```
Input:

root =
                3(dist=0)
               / \
          (-1)2   9(1)
             / \   \
        (-2)4(0)6   8(2)
                   /
                  7(1)

distance_map = {
    0: [3]
    -1: [2]
    1:[9]
    ...
}

* We can NOT do DFS, since we want to preserve the column order from top to bottom as well as from left to right.
```
