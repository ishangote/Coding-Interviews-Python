# 1146. Snapshot Array

## Problem Statement

> Implement a SnapshotArray that supports the following interface:
>
> - `SnapshotArray(int length)` initializes an array-like data structure with the given length. Initially, each element equals 0.
> - `void set(index, val)` sets the element at the given index to be equal to val.
> - `int snap()` takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
> - `int get(index, snap_id)` returns the value at the given index, at the time we took the snapshot with the given snap_id

> Constraints:
>
> - 1 <= length <= 5 \* 10<sup>4</sup>
> - 0 <= index < length
> - 0 <= val <= 10<sup>9</sup>
> - 0 <= snap_id < (the total number of times we call snap())
> - At most 5 \* 10<sup>4</sup> calls will be made to set, snap, and get.

## Examples

Example 1:

```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]

Output: [null,null,0,null,5]

Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

## Brute Force Solution

```
Function Definitions
- SnapshotArray(int length)
- void set(index, val)
- int snap()
- int get(index, snap_id)

- Maintain snapshot of the array in memory:
    {
        snap_id_1: [a, b, p, ...]
        snap_id_2: [a, b, q, ...]
        snap_id_3: [a, b, r, ...]
        ...
    }
- 5 * 10^4 calls to snap function and 5 * 10^4 items in array => 1e9 items not possible to store in memory.
```

## Versioning on Index and Binary Search Solution

```
* We need to implement some kind of versioning
* For each update we can store the snap shot in memory only if the value has changed

> SnapshotArray(3)

snap_id = 0
snapshots = {
    0: [(0, 0)],        * stores (snap_id, value)
    1: [(0, 0)],
    2: [(0, 0)],
}

> set(1, 5)

snap_id = 0
snapshots = {
    0: [(0, 0)],
    1: [(0, 5)],        * Update for snap_id = 0
    2: [(0, 0)],
}

> set(2, 3)

snapshots = {
    0: [(0, 0)],
    1: [(0, 5)],
    2: [(0, 3)],        * Update for snap_id = 0
}

> snap()

snap_id += 1 = 1
snapshots = {
    0: [(0, 0)],
    1: [(0, 5)],
    2: [(0, 3)],
}

> set(1, 9)
snap_id = 1
snapshots = {
    0: [(0, 0)],
    1: [(0, 5), (1, 9)],        * Append new entry for snap_id = 1
    2: [(0, 3)],
}


> set(1, 8)

snap_id = 1
snapshots = {
    0: [(0, 0)],
    1: [(0, 5), (1, 8)],        * Update for snap_id = 1
    2: [(0, 3)],
}

> snap()

snap_id += 1 = 2
snapshots = {
    0: [(0, 0)],
    1: [(0, 5), (1, 8)],
    2: [(0, 3)],
}


> set(1, 10)

snap_id = 2
snapshots = {
    0: [(0, 0)],
    1: [(0, 5), (1, 8), (2, 10)],
    2: [(0, 3)],
}

> get(1, 1)

snapshots = {
    0: [(0, 0)],
    1: [(0, 5), (1, 8), (2, 10)],   <- binary search to find snap_id = 1; return 8
    2: [(0, 3)],
}
Output: 8

```
