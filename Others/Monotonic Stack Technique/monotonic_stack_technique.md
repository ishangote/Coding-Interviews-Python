# Monotonic Stack Technique

A monotonic stack is a stack that is either always increasing or always decreasing. This technique is especially useful for problems that require finding the next/previous greater or smaller elements.

The core idea is to maintain a stack that preserves the desired property (either increasing or decreasing) as we iterate over the array. Whenever this property is violated by a new element, we can "resolve" or "process" the violated conditions, thereby finding relationships like "next greater", "next smaller", etc.

Key Points:

- Monotonic Increasing Stack: This type of stack is used to find the next/previous greater element. The stack keeps elements in increasing order from bottom to top.
- Monotonic Decreasing Stack: This is used to find the next/previous smaller element. The stack keeps elements in decreasing order from bottom to top.
- For next type of problems, iterate over the array from left to right. For previous type of problems, iterate from right to left.

Summary of Monotonic Stack Behavior:

```
Problem             Traversal Direction     Stack
Next Greater	    Left to Right           Decreasing
Previous Greater	Right to Left           Decreasing
Next Smaller	    Left to Right           Increasing
Previous Smaller	Right to Left           Increasing
```

## Time and Space Complexity Analysis

Time Complexity:
For all of the problems, the time complexity is O(n), where n is the number of elements in the array nums. Here's why:

We iterate through the array once.
Each element is pushed onto the stack once and popped from the stack once.
Since each element is processed at most twice (once for the push and once for the pop), the overall time complexity is linear, O(n).

Space Complexity:
The space complexity is O(n) in the worst case, due to the additional stack used to store indices. In the worst case, all elements could end up being pushed onto the stack, leading to a space complexity of O(n).

Thus, for all four problems:

Time complexity: O(n)
Space complexity: O(n)
This analysis applies to the stack-based solution for all variations (next/previous greater/smaller).
