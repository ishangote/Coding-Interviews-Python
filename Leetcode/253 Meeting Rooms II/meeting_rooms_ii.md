# 253. Meeting Rooms II

## Problem Statement

> Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

> Constraints:
>
> - 1 <= intervals.length <= 10<sup>4</sup>
> - 0 <= starti < endi <= 10<sup>6</sup>

## Examples

Example 1:

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

Example 2:

```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## Sweeping Line Algorithm Solution

The sweeping line algorithm is actually a very natural and effective approach for solving this problem. Here’s why:

### How It Works

1. **Event Creation:**  
   For every meeting interval \([start, end]\), create two events:

   - A **start event** (which increases the number of active meetings).
   - An **end event** (which decreases the number of active meetings).

2. **Sorting Events:**  
   Sort all the events by time. When times are equal, process the end event before the start event to correctly reuse rooms.

3. **Sweeping Through Events:**  
   Traverse the sorted events while maintaining a counter of active meetings.
   - Increase the counter at a start event.
   - Decrease it at an end event.  
     The maximum value reached by the counter during this process is the minimum number of conference rooms required.

### Example Walkthrough

Consider the example `[[0,30],[5,10],[15,20]]`:

- **Events:** \((0, +1), (5, +1), (10, -1), (15, +1), (20, -1), (30, -1)\)
- **Processing:**
  - At time 0: count becomes 1.
  - At time 5: count becomes 2.
  - At time 10: count goes back to 1.
  - At time 15: count becomes 2 again.
  - At time 20: count drops to 1.
  - At time 30: count drops to 0.  
    The maximum count is 2, meaning 2 rooms are needed.
