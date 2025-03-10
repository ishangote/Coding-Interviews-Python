# 301. Remove Invalid Parentheses

## Problem Statement

> Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
>
> Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

> Constraints:
>
> - 1 <= s.length <= 25
> - s consists of lowercase English letters and parentheses '(' and ')'.
> - There will be at most 20 parentheses in s.

## Examples

Example 1:

```
Input: s = "()())()"
Output: ["(())()","()()()"]
```

Example 2:

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

Example 3:

```
Input: s = ")("
Output: [""]
```

## Recursive Backtracking Approach

### 1. Preprocessing

- Traverse the input string to calculate how many extra open `(` and close `)` parentheses need to be removed.
- This gives two counters: `open_remove_count` and `close_remove_count`.

### 2. Recursive Backtracking

- **Core Idea:**  
  Use a recursive helper function to process the string character by character.
- **Handling Characters:**
  - **Non-parenthesis characters:**
    - Always added to the current string (`cur`) since they do not affect the balance.
  - **Parenthesis characters:**  
    Two options are explored:
    - **Removal Option:**
      - If removals are available for the current type (open or close), skip the character by calling the recursive function with the removal counter decremented.
    - **Keep Option:**
      - For an open parenthesis `"("`:
        - Append it to `cur` and increment the balance.
      - For a close parenthesis `")"`:
        - Append it only if there is a matching open (i.e., `balance > 0`), then decrement the balance.
- **Base Case:**  
  When the end of the string is reached, if the balance is zero and no removal counts remain, the constructed string is added to the result.

- **Backtracking:**  
  After each recursive call, the last character is removed (using `pop()`) from `cur` to explore alternative paths.

### Memoization (Optional)

We can memoize the state `(idx, balance, open_remove_count, close_remove_count, cur)`.
This memoization optimization helps reduce redundant computations by caching and reusing results for identical states, leading to improved performance in practice.
But it would increase the space complexity.

## Complexity Analysis

### Time Complexity

- **Exponential Branching:**  
  Each parenthesis provides up to 2 choices (remove or keep). If there are `p` parentheses, the worst-case exploration is up to \(O(2^p)\).
- **Per-Call Work:**  
  At each valid solution (leaf node in recursion), joining the characters takes \(O(n)\) time, where \(n\) is the length of the input string.
- **Overall Complexity:**  
  The worst-case time complexity is \(O(n \times 2^p)\). Given the constraints (\(p \leq 20\) and \(n \leq 25\)), the algorithm is tractable.

### Space Complexity

- **Recursion Depth:**  
  The maximum depth of recursion is \(O(n)\) as we process one character at a time.
- **Auxiliary Storage:**
  - The current string (`cur`) uses \(O(n)\) space.
  - The recursion stack can also use up to \(O(n)\) space.
- **Result Storage:**  
  In the worst-case, the number of valid strings (results) can be exponential.
- **Overall Complexity:**  
  The space complexity in the worst-case is \(O(n \times 2^p)\) considering both the recursion stack and the storage for the results.

This backtracking approach effectively explores all valid combinations by pruning invalid paths early and ensuring that each valid string is constructed with the minimum removals necessary.
