# 236. Lowest Common Ancestor of a Binary Tree

## Problem Statement

> Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
> According to the definition of LCA on [Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

> Constraints:
>
> - The number of nodes in the tree is in the range [2, 10<sup>5</sup>].
> - -10<sup>9</sup> <= Node.val <= 10<sup>9</sup>
> - All Node.val are unique.
> - p != q
> - p and q will exist in the tree.

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
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

Example 3:

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Brute Force Solution

```
Input:
root =
             3
          /    \
         5      1
        / \    / \
       6   2  0   8
          / \
         7   4

Approach:
* Find path from root to n1
* Find path from root to n2
* Return the lowest common node

n1 = 5
n2 = 8

n1_path = [3, 5]
n2_path = [3, 1, 8]

lowest common = 3

Output: 3

n1 = 5
n2 = 6

n1_path = [3, 5]
n2_path = [3, 5, 6]

lowest common = 5

Output: 5

n1 = 8
n2 = 1

n1_path = [3, 1, 8]
n2_path = [3, 1]

lowest common = 1

Output: 1
```

## Recursive DFS Solution

```
Input:
root =
             3
          /     \
         6       8
        / \       \
       2   11      13
          / \      /
         9   5    7

n1 = 2
n2 = 5

search 2 or 5 =>

             3
          /     \
    (2)  6  (5)  8
        / \       \
      *2   11(5)   13   * return 2 to parent
          / \      /
         9   5*   7     * return 5 to parent


         (6) 3 (None)
          /     \
      (2)6(5)    8      * found ancestor since left != null and right != null
        / \       \     * return node
       2   11     13
          / \      /
         9   5    7

Output: 6
```

```
Input:
root =
             3
          /     \
         6       8
        / \       \
       2   11      13
          / \      /
         9   5    7

n1 = 8
n2 = 11

search for 8/11 =>

             3 (8)
          /     \
         6 (11)  8*     * return 8 to parent
        / \       \
       2   11*     13   * return 11 to parent
          / \      /
         9   5    7


        (11) 3 (8)      * left is not None and right is not None: return node
          /     \
         6       8
        / \       \
       2   11      13
          / \      /
         9   5    7

Output: 3
```

```
Input:
root =
             3
          /     \
         6       8
        / \       \
       2   11      13
          / \      /
         9   5    7

n1 = 8
n2 = 7

search for 8/7 =>

             3 (8)
          /     \
         6       8*     * return 8 to parent
        / \       \
       2   11      13
          / \      /
         9   5    7


             3 (8)      * left is None right is not None: return right
          /     \
         6       8
        / \       \
       2   11      13
          / \      /
         9   5    7

Output: 8
```

## Approach Summary

To find the Lowest Common Ancestor (LCA) of two nodes p and q in a binary tree, we can use a recursive depth-first search (DFS) approach:

1. Recursive Traversal:

- Start at the root node and recursively traverse the tree.
- If the current node is either p or q, return that node.
- Recursively check the left and right subtrees for p and q.

2. Handling Results from Left and Right Subtrees:

- If both left and right recursive calls return non-null values, the current node is the LCA, because p and q are located in different subtrees.
- If only one subtree returns a non-null value, propagate that node upwards, as it could be the LCA for one of the nodes.

3. Base Cases:

- If the current node is None, return None.
- If the current node is either p or q, return that node.

4. Return the LCA: Once the traversal completes, the node that is returned will be the LCA of p and q.

## References

- https://www.youtube.com/watch?v=13m9ZCB8gjw&t=138s&ab_channel=TusharRoy-CodingMadeSimple
