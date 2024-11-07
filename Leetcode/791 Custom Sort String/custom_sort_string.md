# 791. Custom Sort String

## Problem Statement

> You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
> Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
> Return any permutation of s that satisfies this property.

> Constraints:
>
> - 1 <= order.length <= 26
> - 1 <= s.length <= 200
> - order and s consist of lowercase English letters.
> - All the characters of order are unique.

## Examples

Example 1:

```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

Example 2:

```
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
```

## Solution

```
Example Walkthrough

Input:
order = "bcafg" and s = "abcd"

1. Populate Heap: Traverse s and push characters that exist in order into a min-heap with their priority indices:
min_heap = [(0, 'b'), (1, 'c'), (2, 'a')]

2. Build Result: Characters not in order are directly appended to the result:
    - res = "d"  # 'd' is not in order, so we append it immediately.
    - Next, pop characters from min_heap and add them to res in sorted order:
        res = "dbca"  # final result
```

## Time Complexity Analysis

- Building the Min Heap: For each character in input_string:

  - Checking if the character is in order is O(m), where 𝑚 is the length of order. Since order can have up to 26 characters, this check can be considered O(1) in practice.
  - If the character is in order, finding its index with order.index(char) takes O(m) time.
  - Adding to the heap takes O(logn) time, where n is the number of characters in input_string.

- Building the Result:
  - Popping all characters from the heap and appending them to the result takes O(nlogn) in the worst case, if all characters are in order.

Overall, building the heap takes O(n\*m), where n is the length of input_string and m is the length of order. Since order is limited to 26 characters, we can approximate this to O(n) in practice.

## Approach Summary

1. Min Heap: To prioritize characters in s according to their order in order, use a min-heap to store characters in s with their corresponding index in order.
2. Build the Result: Add characters from the heap in order of priority, followed by characters that don’t appear in order.
