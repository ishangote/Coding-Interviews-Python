# 708. Insert into a Sorted Circular Linked List

## Problem Statement

> Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
> If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.
> If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

> Constraints:
>
> - The number of nodes in the list is in the range [0, 5 \* 10<sup>4</sup>].
> - -10<sup>6</sup> <= Node.val, insertVal <= 10<sup>6</sup>

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/01/19/example_1_before_65p.jpg)

```
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
```

![Explanation 1](https://assets.leetcode.com/uploads/2019/01/19/example_1_after_65p.jpg)

Example 2:

```
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
```

Example 3:

```
Input: head = [1], insertVal = 0
Output: [1,0]
```

## Solution

```
Key Observations
- Inserting in Empty List: If the list is empty, create a node that points to itself and return it.
- Normal Insertion: Traverse until we find a position cur such that cur.val <= insertVal <= cur.next.val.
- Edge Cases with Min/Max Values:
  - If insertVal is smaller than the smallest value or larger than the largest value, insert it at the boundary where values loop around.
  - If all values in the list are identical, any insertion position is valid.
```

```
Example Walkthroughs
Case 1
Input: head = [1, 2, 2, 5], insertVal = 3
Inserting between nodes with values 2 and 5 gives: [1, 2, 2, 3, 5].

Case 2
Input: head = [2, 2, 2, 2], insertVal = 2
Insert anywhere results in: [2, 2, 2, 2, 2].

Edge Cases:
- Insert smaller than all values:
     - Input: head = [1, 2, 2, 5], insertVal = 0
     - Result: [0, 1, 2, 2, 5]

- Insert larger than all values:
     - Input: head = [1, 2, 2, 5], insertVal = 6
     - Result: [1, 2, 2, 5, 6]
```

## Approach Summary

To insert a new value into a sorted circular linked list, start by considering the list’s structure and find the correct spot for insertion. If the list is empty, initialize it with a single node. Otherwise, traverse the list to find a position where the new value fits in sorted order, either between two nodes or at the start/end if it’s the smallest or largest. Return the head after insertion. This solution leverages a two-pointer approach to find the appropriate position.
