# Given an array A of non-negative integers, return True if there exists subset (non-contiguous) that has sum equal to target.
"""
Approach 1: DFS + Backtracking:

 0  1  2  3  4
[1, 4, 5, 3, 2] target = 6
1 + 4 + 5 + 3 + 2 = max_sum = 15

                                    [0, 15]
                                    /
                                [1, 14]
                                /       \
                         [1+4=5, 10]    [1+5=6, 9]   
                        /    |       \
              [5+5=10, 5] [5+3=8, 7] [5+2=7, 8]

Approach 2: Dynamic Programming

 0  1  2  3  4
[2, 3, 7, 8, 10], num = 11

if num = 0 then empty subset will always exist



       0 1 2 3 4 5 6 7 8 9 10 11
0 (2)  T F T F F F F F F F F  F
1 (3)  T F T T F T F F F F F  F
2 (7)  T F T T F T F T F T T  F
3 (8)  T F T T F T F T T T T  T
4 (10) T F T T F T F T T T T  T

RULES:
1. if dp[row] > dp[col]: dp[row][col] = dp[row-1][col]
2. else: dp[row-1][col] OR one row up and arr[row] steps back

"""
def subset_sum(arr, num):

    if num < 0 or len(arr) == 0 or not arr: return None

    rows = len(arr)
    cols = num + 1

    memo = [[False for idx in range(cols)] for idx1 in range(rows)]
    for idx in range(rows): memo[idx][0] = True
    for idx in range(cols): if arr[0] == idx: memo[0][idx] = True

    for idx1 in range(1, rows):
        for idx2 in range(1, cols):
            if idx2 >= arr[idx1]: memo[idx1][idx2] = memo[idx1 - 1][idx2] or memo[idx1 - 1][idx2 - arr[idx1]]
