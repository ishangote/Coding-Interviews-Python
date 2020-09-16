vc '''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4

1 <= nums.length <= 100
1 <= nums[i] <= 100

count = 0

 0 1 2 3 4 5
[1,2,3,1,1,3]
           ^
           
(0, 3), (0, 4) (3, 4) (2, 3)

ans = 4

map = {
1: 2
2: 1
3: 1


 0 1 2 3
[1,1,1,1]
       ^
 
 (0,1), (0,2) (1, 2) (0,3) (1,3) (2,3)
 ans = 6

 map 
 {
 1:3
 }
 
 counts_arr = 
  1................100
 [2                   ]

'''

def good_pairs(nums):
    counts = {}
    ans = 0
    for val in nums:
        if val not in counts:
            counts[val] = 1
        else:
            ans += counts[val]
            counts[val] += 1
    return ans
    
"""
 In        Expected        Actual
 [1]        0                0
 
 [1, 1]     1                1
 
 [1, 2, 3]   0               0
 
ans = 0
{
     1:1
     2:1
     3:1
}
"""