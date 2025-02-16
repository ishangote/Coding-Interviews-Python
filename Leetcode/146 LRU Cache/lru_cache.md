# 146. LRU Cache

## Problem Statement

> Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
>
> Implement the LRUCache class:
>
> - `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
> - `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
> - `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
>
> The functions `get` and `put` must each run in `O(1)` average time complexity.

> Constraints:
>
> - 1 <= capacity <= 3000
> - 0 <= key <= 10<sup>4</sup>
> - 0 <= value <= 10<sup>5</sup>
> - At most 2 \* 10<sup>5</sup> calls will be made to get and put.

## Examples

Example 1:

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4
```

## LRU Cache Implementation Summary

### Approach:

The LRU (Least Recently Used) Cache is implemented using a Doubly Linked List (DLL) and a Hash Map (Dictionary) to achieve O(1) time complexity for both get and put operations.

### Design:

**Doubly Linked List (`DLL`)**:

- Nodes store `(key, value)`.
- Maintains ordering of items based on access (Most Recently Used (MRU) at the head, Least Recently Used (LRU) at the tail).
- Supports efficient removal and addition of nodes.

**Hash Map (`hm`)**:

- Maps `key` → `DLLNode`, allowing `O(1)` lookup for any key.

### Operations:

1. `get(key)`:

   - If key exists in `hm`, move the node to the head (making it MRU).
   - Return the value.
   - Otherwise, return `-1`.

2. `put(key, value)`:

   - If key already exists, remove the old node from `DLL` and `hm`.
   - If the cache is full, remove the tail.prev node (LRU item) from both `DLL` and `hm`.
   - Insert a new node at the head of `DLL` (MRU position) and update `hm`.

### Key Functions:

- `move_node_to_head(node)` → Moves accessed node to head (MRU).
- `delete_node(node)` → Deletes a node from DLL and updates size.
- `add_heads_next(key, value)` → Adds new node right after head.

### Edge Cases Handled:

- `put` replaces value if key exists.
- `get` marks an accessed node as MRU.
- Evicts only when capacity is reached.
- Cache operations maintain `O(1)` complexity.

### Implementation Recap

- Delete from tail (LRU).
- Insert at head (MRU).
- Hash Map (`hm`) for fast lookups.
- Doubly Linked List (`dll`) for efficient ordering.

This structure ensures fast access, insertion, and eviction while maintaining the correct order of usage.
