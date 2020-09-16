"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""

"""
  0 1 2 3  4  5
[-1,0,1,2,-1,-4]

Sort O(nlogn)

  0  1  2 3 4 5
[-4,-1,-1,0,1,2]
  i
     l     
              h
    
"""
def three_sum(nums):
    nums.sort()
    ans = []
    for idx in range(len(nums) - 2):
        if nums[idx] > 0: return ans
        if idx == 0 or nums[idx - 1] != nums[idx]:
            lo, hi = idx + 1, len(nums) - 1
            while lo < hi:
                if nums[idx] + nums[lo] + nums[hi] == 0: 
                    ans.append([nums[idx], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1

                elif nums[idx] + nums[lo] + nums[hi] < 0:
                    lo += 1

                else: hi -= 1

    return ans

"""
        In      Expect      Actual
        [1]     []          []
        []      []          []
[-1, 2, -1]     [[-1, -1, 2]] [[-1, -1, 2]]
  
  0  1 2
[-1,-1,2]                    [[-1, -1, 2]]
  i
       l
       h

 0  1  2  3
[0, 0, 0, 0]
 i


"""
