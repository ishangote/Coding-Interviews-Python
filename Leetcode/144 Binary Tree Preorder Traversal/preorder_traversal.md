# 144. Binary Tree Preorder Traversal

## Problem Statement

> Given the root of a binary tree, return the preorder traversal of its nodes' values.

## Examples

Example 1:

```
        1
         \
          2
         /
        3

Input: root = [1,null,2,3]
Output: [1,2,3]
```

Example 2:

```
                    1
                  /   \
                2      3
               / \      \
              4   5      8
                 /  \     \
                6    7     9

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]

```

Example 3:

```
Input: root = []
Output: []

```

## DFS Recursive Solution

- Pre-order traversal => Root -> Left -> Right

```
Input:
                    1* res = [1]
                  /   \
                 2     3
                / \     \
               4   5     8
                  / \     \
                6    7     9


                    1
                  /   \
res = [1, 2]    *2     3
                / \     \
               4   5     8
                  / \     \
                6    7     9


                    1
                  /   \
                 2     3
                / \     \
res=[1, 2, 4] *4   5     8
                  / \     \
                6    7     9

Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]
```

## Iterative Solution

- Pre-order traversal => Root -> Left -> Right

```
Input:
                    1
                  /   \
                 2     3
                / \     \
               4   5     8
                  / \     \
                6    7     9

res = []
stack = [1]

node = 1
res = [1]
stack = [3, 2]

node = 2
res = [1, 2]
stack = [3, 5, 4] * node.right pushed first then node.left

node = 4
res = [1, 2, 4]
stack = [3, 5]

node = 5
res = [1, 2, 4, 5]
stack = [3, 5, 7, 6]
...
```
