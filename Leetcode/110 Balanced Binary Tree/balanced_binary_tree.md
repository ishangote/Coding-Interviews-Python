# 110. Balanced Binary Tree

## Problem Statement

> A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
> Given a binary tree, determine if it is height-balanced.

> Constraints:
>
> - The number of nodes in the tree is in the range [0, 5000].
> - -104 <= Node.val <= 104

## Examples

Example 1:

```
        3
       / \
      9  20
        /  \
       5    7

Input: root = [3,9,20,null,null,15,7]
Output: true
```

Example 2:

```
         1
        / \
       2   2
      / \
     3   3
    / \
   4   4

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

Example 3:

```
Input: root = []
Output: true
```

## Brute Force

```
Example 1:
root =
        3*
       / \
      9  20
        /  \
       5    7

max_left_height = 1
max_right_height = 2

* For each node calculate max_left_height and max_right_height recursively
* if abs(max_left_height - max_right_height) <= 1 => it is a balanced binary tree

Output: True
```

## Optimization

- Recursive function can return the max height as well as if the binary tree is balanced or not
- Bottom up traversal

Example 1:

```
root =
        1* => is balanced if root.left is balanced and root.right is balanced
       / \
      2   2
     / \   \
    3   3   3
   /         \
  4           4


root =
        1
       / \
      2   2
     / \   \
    3   3   3
   /         \
  4           4* => left height = 0, right height = 0 return (1 + max(0, 0), true)



        1
       / \
      2   2
     / \   \
    3   3   3* left height = 0, right height = 1 return (1 + max(0, 1), true)
   /         \
  4           4


        1
       / \
      2   2* left height = 0 right height = 2 return (1 + max(0, 2), false)
     / \   \
    3   3   3
   /         \
  4           4

Output: False
```

## References

- [Leetcode](https://leetcode.com/problems/balanced-binary-tree/description/)
- [Youtube](https://youtu.be/QfJsau0ItOY?si=EbemvAxHHxMM-yug)
