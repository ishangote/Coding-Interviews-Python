# 243. Shortest Word Distance

## Problem Statement

> Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

> Constraints:
>
> - 2 <= wordsDict.length <= 3 x 10<sup>4</sup>
> - 1 <= wordsDict[i].length <= 10
> - wordsDict[i] consists of lowercase English letters.
> - word1 and word2 are in wordsDict.
> - word1 != word2

## Examples

Example 1:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
```

Example 2:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

## Brute Force

```
Input:
word1 = "makes",
word2 = "coding"
wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]

Algorithm:
* For every occurrence of word 1
    * Iterate over entire array to find all occurrences of word 2

* Time: O(n^2), where n => length of wordsDict
* Space: O(1)

Output: 1
```

## Two Pointers Optimized Solution

- Store the most recent location of word 1 and word 2

```
Input:

word1 = "makes",
word2 = "coding"

wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]
     ^
idx1 = -1
idx2 = -1


wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]
                ^
idx1 = 1
idx2 = -1


wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]
                          ^
idx1 = 1
idx2 = -1


wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]
                                    ^
idx1 = 1
idx2 = 3
shortest_distance = 2


wordsDict =
     0          1        2          3         4
["practice", "makes", "perfect", "coding", "makes"]
                                              ^
idx1 = 4
idx2 = 3
shortest_distance = 1
```
