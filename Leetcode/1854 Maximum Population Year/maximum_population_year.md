# 1854. Maximum Population Year

## Problem Statement

> You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
> The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
> Return the earliest year with the maximum population.

> Constraints:
>
> 1 <= logs.length <= 100
> 1950 <= birthi < deathi <= 2050

## Examples

Example 1:

```
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
```

Example 2:

```
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
```

## Sweep Line Algorithm Solution

**Motivation**:
The sweep line algorithm efficiently processes problems involving intervals or events by "sweeping" through a sorted sequence of events. It is ideal for finding overlaps, intersections, and other cumulative properties over a one-dimensional domain.

**Method**:

1. Event Generation:
   - Convert each interval or event into a start event (e.g., +1) and an end event (e.g., -1 or at end + 1 for inclusivity).
2. Sorting:
   - Sort the events by their coordinate or time value.
3. Sweeping:
   - Traverse the sorted events, updating a running state (e.g., a counter) based on each event's value.
   - Track key information like the maximum state and its corresponding position.
4. Result Extraction:
   - Use the recorded data to output the final answer (e.g., the point with maximum overlap).

**Reflection**:

- Efficiency: O(nlogn) due to sorting and O(n) for processing.
- Versatility: Applicable to various problems like maximum population, interval intersections, and collision detection.
- Design Considerations: Ensure proper handling of endpoints and simultaneous events for accurate results.
