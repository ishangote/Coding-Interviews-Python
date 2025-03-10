# 139. Word Break

## Problem Statement

> Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
> Note that the same word in the dictionary may be reused multiple times in the segmentation.
> You may assume the dictionary does not contain duplicate words

> Constraints:
>
> - 1 <= s.length <= 300
> - 1 <= wordDict.length <= 1000
> - 1 <= wordDict[i].length <= 20
> - s and wordDict[i] consist of only lowercase English letters.
> - All the strings of wordDict are unique.

## Examples

Example 1:

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

Example 3:

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Top-Down Solution

- We use recursion with memoization to determine if a string can be segmented into words from a given dictionary.
- The function checks each possible prefix of the string, and if the prefix is a valid word, it recursively processes the remaining suffix.
- A memoization dictionary stores results for previously computed substrings to optimize redundant calls.
- Time complexity: O(n^2) =>
  - There are O(n) recursive calls (one per suffix), and each checks up to O(n) prefixes.
- Space complexity: O(n) =>
  - Memoization => We store the result for each unique suffix of s in memo.
  - In the worst case, we could store results for every substring starting at each position in s, which leads to O(n) space.
