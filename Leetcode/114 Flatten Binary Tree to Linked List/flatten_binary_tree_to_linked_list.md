# 114. Flatten Binary Tree to Linked List

## Problem Statement

> Given the root of a binary tree, flatten the tree into a "linked list"
>
> The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
>
> The "linked list" should be in the same order as a pre-order traversal of the binary tree.

```
Example 1:
Input:
        1
      /   \
     2     5
    / \     \
   3   4     6

Output:
        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
```

> Constraints:
>
> - The number of nodes in the tree is in the range [0, 2000].
> - -100 <= Node.val <= 100

## DFS Solution

```
Example 1:
Input:
    1

Output:
    1

----------------------------------------

Example 2:
Input:
    1
   /
  2

Output:
    1
     \
      2

----------------------------------------

Example 3:
Input:
    1
     \
      2

Output:
    1
     \
      2

* if right sub-tree is already flattened then don't do anything

----------------------------------------

Example 4:
Pre-order traversal: Root -> Left -> Right
Pre-order: 1 2 3

Input:
        1
      /   \
     2     3


Output:
        1
         \
          2
           \
            3

* left sub-tree is flattened and moved to root.right

----------------------------------------

Example 5:
Pre-order traversal: Root -> Left -> Right
Pre-order: 1 2 3

Input:
        1
      /   \
     2     5
    / \   / \
   3   4  6  7

Some recursive DFS needs to be implemented, where base case can be:

* if not node: return None
* if not node.left and not node.right: return node

* Flatten left sub tree
* Flatten right sub tree
* node.right must become node.left
* node.left must become None
* The left tail of the flattened left sub-tree must point to right sub-tree root

      1
       \  (node.left must become node.right)
        \
       _______
      |   2   |
      |  / \  |  (flatten_helper(node.left)) ->  must flatten left sub-tree and return the tail of the Linked List i.e node = 4
      | 3   4 |
      |_______|
          \
           \
         _________
        |    5    |
        |   / \   |  (flatten_helper(node.right)) -> must flatten right sub-tree and return tail of the Linked List i.e node = 7
        |  6   7  |
        |_________|



* The tail of the node is flattened right sub-tree tail OR the flattened left sub tree tail OR the node itself

Output:
        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
                   \
                    7
```
