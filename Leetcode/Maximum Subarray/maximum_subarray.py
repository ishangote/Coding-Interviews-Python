#Given an integer array nums, find the contiguous subarray (containing at least one number) 
#which has the largest sum and return its sum.

"""
Questions:
1. len(subarray) == 1? Yes
2. len(nums) ==0? No

Examples:

  0 1  2 3  4 5 6  7 8
[-2,1,-3,4,-1,2,1,-5,4]

-2
-2, 1
-2, 1, -3
...

num of subarrays = n * (n + 1) / 2

Time: O(n^2)
Space: O(1)

To track maximum sum of a subarr starting at index i 
  0 1  2 3  4 5 6  7 8
[-2,1,-3,4,-1,2,1,-5,4]
                     i
max_subarr_sums = 
[-2,1,-2,4,3,5,6,1,5]

Time: O(n)
Space: O(n)

Optimization on space:
track cur_subarr_sum, max_sum

Dynamic Programming Rule (Kadane Algo):
cur_subarr_sum = max(cur_subarr_sum + nums[i], nums[i])
max_sum = max(max_sum, cur_subarr_sum)
"""
import sys
def maximum_subarray(nums):
    cur_subarr_sum, max_sum = -sys.maxsize, -sys.maxsize
        
    for idx in range(len(nums)):
        cur_subarr_sum = max(cur_subarr_sum + nums[idx], nums[idx])
        max_sum = max(max_sum, cur_subarr_sum)
    
    return max_sum

if __name__ == "__main__":
    nums = []
    n = int(input("Enter length of nums: "))
    for itr in range(n):
        num = int(input("Enter an integer: "))
        nums.append(num)
    print("Maximum Subarray Sum: " + str(maximum_subarray(nums)))