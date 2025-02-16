# 138. Copy List with Random Pointer

## Problem Statement

> A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
>
> Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
>
> For example, if there are two nodes X and Y in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.
>
> Return the head of the copied linked list.
>
> The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
>
> `val`: an integer representing Node.val
> `random_index`: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
> Your code will only be given the head of the original linked list.

> Constraints:
>
> - 0 <= n <= 1000
> - -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
> - Node.random is null or is pointing to some node in the linked list.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

Example 3:

![Example 3](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

---

## **Approach 1: Using Hash Map**

### **Algorithm**

1. **First Pass**: Create a copy of each node and store it in a **hash map** (`copy_nodes[cur] = copied_node`).
2. **Second Pass**: Set up `.next` and `.random` pointers using the hash map.
3. **Return** the copied head.

```
    |----------->
1   2   3   4   5
|_______^       |
    ^___________|


Approach 1: O(n) Time O(n) space

use hashmap to store [original:clone] map
First Pass
hm = {1:1', 2:2', 3:3', 4:4', 5:5'}
Second Pass
connect next pointers and random pointers
```

### **Complexity**

- **Time Complexity**: `O(n)`, as we iterate through the list twice.
- **Space Complexity**: `O(n)`, due to the additional hash map.

---

## **Approach 2: Optimized O(1) Space**

### **Algorithm**

1. **First Pass**: Insert a **copy of each node** right after the original node (`A → A' → B → B' → C → C'`).
2. **Second Pass**: Assign the `.random` pointers for copied nodes (`A'.random = A.random.next`).
3. **Third Pass**: **Separate the two lists** (original and copied).
4. **Return** the copied head.

```
Approach 2: O(n) Time O(1) space

First Pass
1   2   3   4   5

1'  2'  3'  4'  5'

Second Pass: Assign random pointers
1   2   3   4   5
| / | / | / | / |
1'  2'  3'  4'  5'

Third Pass (Restore second list)
*
1   2   3   4   5
| / | / | / | / |
1'  2'  3'  4'  5'

--------------------------------------------------

1 -> 2 -> 3 -> 4 -> None
v    v    v    v
3    1    3    2


1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> None
v    v    v    v    v    v    v    v
3         1         3         2
```

### **Complexity**

- **Time Complexity**: `O(n)`, since we iterate the list three times.
- **Space Complexity**: `O(1)`, as no extra hash map is used.

---
