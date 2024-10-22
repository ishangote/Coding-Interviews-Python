# 2222. Number of Ways to Select Buildings

## Problem Statement

> You are given a 0-indexed binary string s which represents the types of buildings along a street where:
>
> - s[i] = '0' denotes that the ith building is an office and
> - s[i] = '1' denotes that the ith building is a restaurant.
>
> As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

> - For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
>
> Return the number of valid ways to select 3 buildings.

> Constraints:
>
> - 3 <= s.length <= 10<sup>5</sup>
> - s[i] is either '0' or '1'.

## Examples

Example 1:

```
Input: s = "001101"
Output: 6
Explanation:
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
```

Example 2:

```
Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
```

## Brute Force Solution

```
Input:
nums =
 0 1 2 3 4 5
"0 0 1 1 0 1"
 ^
     *

* Find subsequences of length 3
* Return count of alternating subsequences

Output:
6
```

## Optimization

```
Input:
nums = "000"
Output:
0

Input:
nums = "0001"
Output:
0
```

```
All possible subsequences of length 3 =>

000
001
010     -> valid
100
101     -> valid
110
111

* need to find subsequences of length 3 which are equal to either 010 or 101


Input:
nums =
"0 0 1 1 0 1"
   ^
* if idx = 1 (0) is to be considered as the middle 0 of 101, then we need to count number of 1's to the right and left

nums =
"0 0 1 1 0 1"
     ^
* if idx = 2 (1) is to be considered as the middle 1 of 010, then we need to count number of 0's to the right and left

right_0s = 2
left_0s = 1
# valid subsequences possible = 2 * 1 = 2


       0 1 2 3 4 5
nums = 0 0 1 1 0 1
                 ^
count = 3
left_zeroes = [-1, -1, 2, 2, -1, 3]


       0 1 2 3 4 5
nums = 0 0 1 1 0 1
       ^
count = 3
right_zeroes = [-1, -1, 1, 1, -1, 0]


       0 1 2 3 4 5
nums = 0 0 1 1 0 1
                 ^
count = 3
left_ones = [0, 0, -1, -1, 2, -1]


       0 1 2 3 4 5
nums = 0 0 1 1 0 1
       ^
count = 3
right_ones = [3, 3, -1, -1, 1, -1]


* Compute subsequences (010)
                 0   1  2  3   4  5
nums =         [ 0   0  1  1   0  1]
left_zeroes =  [-1, -1, 2, 2, -1, 3]
right_zeroes = [-1, -1, 1, 1, -1, 0]


for each 1
   res += (left_zeroes[idx] * right_zeroes[idx])

* Compute subsequences (101)
              0   1   2   3  4   5
nums =       [0   0   1   1  0   1]
left_ones =  [0,  0, -1, -1, 2, -1]
right_ones = [3,  3, -1, -1, 1, -1]

for each 0
   res += (left_ones[idx] * right_ones[idx])

Output:
6
```
