# 1650. Lowest Common Ancestor of a Binary Tree III

## Problem Statement

> Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
> Each node will have a reference to its parent node. The definition for Node is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

> According to the definition of LCA on [Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

> Constraints:
>
> - The number of nodes in the tree is in the range [2, 10<sup>5</sup>].
> - -10<sup>9</sup> <= Node.val <= 10<sup>9</sup>
> - All Node.val are unique.
> - p != q
> - p and q exist in the tree.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
```

Example 3:

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Solution

```
Input:
root =
             3
          /     \
         6       8
        / \       \
       2*  11      13
          / \      /
         9   5*   7

n1 = 2
n2 = 5

n1 height = 2       * compute height by moving up until parent == None
n2 height = 3

* Move pointer to n2 up till n1 height = n2 height
* Keep moving up until n1 pointer = n2 pointer

Output: 6
```

## Approach Summary

1. Calculate Heights: Start from each node and move up the tree to calculate its height (distance to the root). This gives the relative depths of both nodes.
2. Equalize Heights: Adjust the starting position of the deeper node by moving it up to match the height of the shallower node. This ensures both nodes are at the same level in the tree.
3. Move Up Simultaneously: From this equalized height, move both nodes up the tree one step at a time until they meet. The meeting point is their lowest common ancestor.
