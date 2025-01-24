# 729. My Calendar I

## Problem Statement

> You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
>
> A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
>
> The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
>
> Implement the MyCalendar class:
>
> - MyCalendar() Initializes the calendar object.
> - boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

> Constraints:
>
> - 0 <= start < end <= 10<sup>9</sup>
> - At most 1000 calls will be made to book.

## Examples

Example 1:

```
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

## Brute Force Solution

```
Input       Output
[10, 20) -> true
[5, 10)  -> true
[20, 30) -> true

New Interval:
[15, 30)    -> expected false

Existing intervals: Iterate over each interval
[[10, 20), [5, 10), [20, 30)]
     ^
     * overlaps [15, 30) -> return false

Two intervals overlap if:
1. The start of one interval is less than the end of the other.
2. This condition needs to be true for both intervals.

Condition: Two intervals `[start1, end1)` and `[start2, end2)` overlap if: `start1 < end2 and start2 < end1`
```

## Binary Search Tree Solution

```
Example 1:
* Maintain a BST to store intervals

          [10, 20)
          /      \
  [5, 10)         [20, 30)    * All nodes to the left of root contain intervals lte 10
                              * All nodes to the right of root contain intervals gte 20


New Interval
[22, 50)

          [10, 20)       * not overlapping -> move right since 22 >= 20
          /      \
  [5, 10)         [20, 30) -> * overlapping intervals => return False



New Interval
[3, 5)

        [10, 20)    -> * not overlapping -> move left since 5 <= 10
          /      \
  [5, 10)         [20, 30)
     * not overlapping -> move left since 5 <= 5 -> insert new node


        [10, 20)
          /      \
  [5, 10)         [20, 30)
   /
[3, 5)    => return True

```
