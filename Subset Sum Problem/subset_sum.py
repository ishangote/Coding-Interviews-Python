# Given an array A of non-negative integers, return True if there exists subset (non-contiguous) that has sum equal to target.
"""
 0  1  2  3  4
[1, 4, 5, 3, 2] target = 6 


memo
    j
i   0 1 2 3 4 5 6
0 1 T T F F F F F
1 4 T T F F T 
2 5 T
3 3 T
4 2 T

"""
def subset_sum(arr):