# 501. Find Mode in Binary Search Tree

## Problem Statement

> Given the root of a binary search tree (BST) with duplicates, return all the [mode(s)](<https://en.wikipedia.org/wiki/Mode_(statistics)>) (i.e., the most frequently occurred element) in it.
>
> If the tree has more than one mode, return them in any order.
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys less than or equal to the node's key.
> - The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
> Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

> Constraints:
>
> - The number of nodes in the tree is in the range [1, 104].
> - -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>

## Examples

Example 1:

```
Input:
        3
      /   \
     1     3
    /  \
   1    2
         \
          3

Output:
[3]
```

## Brute Force Solution

```
Input:
        3*
      /   \
     1     3
    /  \
   1    2
         \
          3

count = {
    3: 1
}

        3
      /   \
     1*    3
    /  \
   1    2
         \
          3

...     (Parse entire tree and maintain frequency in count)

count = {
    3: 3
    1: 2
    2: 1
    5: 1
}

Output:
[1, 3]
```

## In-order Traversal Solution

- In-order traversal (Left - Root - Right) of BST results in a sorted array

```
Input:
root =
        3
      /   \
     1     3
    /  \
   1    2
  /      \
 1        3


In-order traversal:
1 -> 1 -> 1-> 2 -> 3 -> 3 -> 3

* Need to visualize how we will find the result given a sorted array: [1, 1, 1, 2, 3, 3, 3]

arr =
[1, 1, 1, 2, 3, 3, 3]

cur = 0
cur_freq = 0
max_freq = 0
res = []


arr =
[1, 1, 1, 2, 3, 3, 3]
 ^
cur = 0 => 1
cur_freq = 0 => 1
max_freq = 0 => 1
res = [] => [1]         * update res since cur_freq > max_freq


arr =
[1, 1, 1, 2, 3, 3, 3]
    ^
cur = 1
cur_freq = 2
max_freq = 2
res = [1]


arr =
[1, 1, 1, 2, 3, 3, 3]
       ^
cur = 1
cur_freq = 3
max_freq = 3
res = [1]


arr =
[1, 1, 1, 2, 3, 3, 3]
          ^
cur = 1 => 2                  * since cur != ^
cur_freq = 3 => 1             * reset cur_freq to 1
max_freq = 3
res = [1]                     * do not update since cur_freq < max_freq


arr =
[1, 1, 1, 2, 3, 3, 3]
             ^
cur = 2 => 3                  * since cur != ^
cur_freq = 1 => 1             * reset cur_freq to 1
max_freq = 3
res = [1]                     * do not update since cur_freq < max_freq


arr =
[1, 1, 1, 2, 3, 3, 3]
                ^
cur = 3
cur_freq = 2                  * increment cur_freq
max_freq = 3
res = [1]


arr =
[1, 1, 1, 2, 3, 3, 3]
                   ^
cur = 3
cur_freq = 3                  * increment cur_freq
max_freq = 3
res = [1] => [1, 3]           * add 3 to res since cur_freq == max_freq
```

#### Issue with Mutability in Recursive Functions

- Problem:
  In recursive functions, immutable objects like integers (e.g., cur, cur_freq, max_freq) do not retain their updated values across recursive calls. In the given example, updates to these variables inside the inorder_helper function do not persist, leading to incorrect results.

```
# THIS CODE WILL FAIL
def inorder_helper(node, cur, cur_freq, max_freq, res):
    if not node:
        return

    inorder_helper(node.left, cur, cur_freq, max_freq, res)

    if cur != node.value:
        cur = node.value
        cur_freq = 0

    cur_freq += 1

    if cur_freq > max_freq:
        res = [cur]

    elif cur_freq == max_freq:
        res.append(cur)

    else:
        pass

    inorder_helper(node.right, cur, cur_freq, max_freq, res)


# Time: O(n), where n => number of nodes in BT
# Space: O(1), excluding the implied call stack memory for recursion
def bst_mode_inorder(root):
    res = []
    cur, cur_freq, max_freq = -sys.maxsize, 0, 0

    inorder_helper(root, cur, cur_freq, max_freq, res)

    return res
```

- Why It Failed:
  - Immutable objects (e.g., integers) create new copies in each recursive call, so changes are not reflected across calls.
  - Only mutable objects (e.g., lists) retain changes across recursive calls.
    Solution: Wrap immutable variables in a mutable container (like a list) to ensure updates persist. Here's the fixed version using lists:
