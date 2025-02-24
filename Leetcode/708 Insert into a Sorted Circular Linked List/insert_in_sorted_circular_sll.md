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

CASE 1: Normal Case => cur.value <= target <= cur.next.value

Input:
insert(4)
      __________________________
     v                          |
     2 -> 5 -> 6 -> 9 -> 20 -> 35
                    *
                    head
Output:
      ______________________________
     v                              |
     2 -> 4 -> 5 -> 6 -> 9 -> 20 -> 35
                         *
                         head
```

```
CASE 2: insertVal is smaller than the smallest value OR larger than the largest value =>

- when we reach the largest number i.e cur.value > cur.next.value
- check if target >= cur.value OR target <= cur.next.value
- add node after cur

Input:
insert(1)
      __________________________
     v                          |
     2 -> 5 -> 6 -> 9 -> 20 -> 35
                    *
                    head
Output:
    ______________________________
   v                              |
   1 -> 2 -> 5 -> 6 -> 9 -> 20 -> 35
                       *
                       head

                       OR

Input:
insert(40)
      __________________________
     v                          |
     2 -> 5 -> 6 -> 9 -> 20 -> 35
                    *
                    head
Output:
      _______________________________
     v                               |
     2 -> 5 -> 6 -> 9 -> 20 -> 35 -> 40
                    *
                    head
```

```
CASE 3: Univalued List =>
- if we reach head again
- no above condition matched => insert after head

Input:
insert(0)
      ______________
     v              |
     2 -> 2 -> 2 -> 2
          *
          head

Output:
      ___________________
     v                   |
     2 -> 2 -> 0 -> 2 -> 2
          *
          head

               OR

Input:
insert(9)
      ______________
     v              |
     2 -> 2 -> 2 -> 2
          *
          head

Output:
      ___________________
     v                   |
     2 -> 2 -> 9 -> 2 -> 2
          *
          head
```

## References

- https://www.youtube.com/watch?v=XN9OsmP2YTk&ab_channel=CrackingFAANG
