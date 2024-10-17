# 2055. Plates Between Candles

## Problem Statement

> There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '\*' and '|' only, where a '\*' represents a plate and a '|' represents a candle.
>
> You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.
>
> For example, s = "||\*\*||\*\*|\*", and a query [3, 8] denotes the substring "\*||\*\*|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
> Return an integer array answer where answer[i] is the answer to the ith query.

> Constraints:
>
> - 3 <= s.length <= 10<sup>5</sup>
> - s consists of '\*' and '|' characters.
> - 1 <= queries.length <= 10<sup>5</sup>
> - queries[i].length == 2
> - 0 <= lefti <= righti < s.length

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/10/04/ex-1.png)

```
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/10/04/ex-2.png)

```
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
```

## Brute Force Solution

```
s =
0 1 2 3 4 5 6 7 8 9
* * | * * | * * * |


query (0, 5)

s =
0 1 2 3 4 5 6 7 8 9
* * | * * | * * * |
-----------
    ^
      *     count = 1

s =
0 1 2 3 4 5 6 7 8 9
* * | * * | * * * |
-----------
    ^
          *     count = 2

* For each query, iterate over the range to compute plates
```

## Optimized solution

```
* A brute force approach would be too slow due to the potential size of the input and the number of queries.
* Preprocessing the string to optimize queries will be essential.

s =
0 1 2 3 4 5 6 7 8 9
* * | * * | * * * |

* Number of plates seen till idx
prefix_sum_plates =
 0  1  2  3  4  5  6  7  8  9
[1, 2, 2, 3, 4, 4, 5, 6, 7, 7]

* nearest candle to the left of idx
nearest_left_candles =
  0   1  2  3  4  5  6  7  8  9
[-1, -1, 2, 2, 2, 5, 5, 5, 5, 9]

* nearest candle to the right of idx
nearest_right_candles =
 0 1  2  3  4  5  6  7  8  9
[2 2  2  5  5  5  9  9  9  9]

* plates in between would be the difference between prefix_sum[closest_candle_right] and prefix_sum[closest_candle_left]

* For each query [left, right], find the nearest candle within the range

Example:
query (1, 7) =>
s =
0 1 2 3 4 5 6 7 8 9
* * | * * | * * * |
  -------------
  l           h

nearest candle to the right of l => nearest_right_candles[l] (2)
nearest candle to the left of h => nearest_left_candle[h] (5)
plates in between = prefix_sum_plates[5] - prefix_sum_plates[2] = 4 - 2 = 2
```
