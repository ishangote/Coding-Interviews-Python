# 145. Binary Tree Postorder Traversal

## Problem Statement

> Given the root of a binary tree, return the postorder traversal of its nodes' values.

## Examples

Example 1:

```
        1
         \
          2
         /
        3

Input: root = [1,null,2,3]
Output: [3,2,1]
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
Output: [4,6,7,5,2,9,8,3,1]

```

Example 3:

```
Input: root = []
Output: []

```

## DFS Recursive Solution

- Post-order traversal: Left -> Right -> Root

```
Input:
                    1* res = []
                  /   \
                 2     3
                / \     \
               4   5     8
                  / \     \
                6    7     9

                    1
                  /   \
         res=[] *2     3
                / \     \
               4   5     8
                  / \     \
                6    7     9

                    1
                  /   \
                 2     3
                / \     \
    res = [4] *4   5     8
                  / \     \
                6    7     9


                    1
                  /   \
                 2     3
                / \     \
    res = [4]  4  *5     8
                  / \     \
                6    7     9

                    1
                  /   \
                 2     3
                / \     \
               4   5     8
                  / \     \
   res = [4, 6] *6   7     9
...

Output: [4, 6, 7, 5, 2, 9, 8, 3, 1]
```

## (TODO) Iterative Solution
