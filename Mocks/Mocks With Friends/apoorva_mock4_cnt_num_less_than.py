'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
0 <= nums[i] <= 100
2 <= nums.length <= 500
'''

"""
 0 1 2 3 4
[8,1,2,2,3]        =>  [4,0,1,1,3]
 *
 0  1. 2. 3. 4
[1, 2, 2, 3, 8]
             *
       
count = {
    1: 0
    2: 1
    3: 3
    8: 4
}

[8,1,2,2,3]
         *
ans = [4, 0, 1, 1, 3]
       
 0 1 2 3
[8,1,2,2,3]
 *

0: 0 
1: 1 
2: 2 
3: 1 
...

8: 1

[8,1,2,2,3]
   *
   
prev_count = 3
1: 0
2: 1
3: 3
8: 4

[8,1,2,2,3]
         *
 
counts = 
 0 1 2 3 4 6 7 8... 100
[0 1 2 1 0 0 0 1  0000]
     *
tmp = 
 0 1 2 3 4 5 6 7
[0 0 1 3 4 4 4 4] 
prev_count = 1

[8,1,2,2,3]
 *


ans = 
 0 1 2 3 4
[4 0         ]
"""

def count_nums(nums):    
    counts = [0 for i in range(101)]
    
    # Count nums
    for n in nums:
        counts[n] += 1
    
    prev_count = 0
    for idx, c, in enumerate(counts): 
        tmp = c
        counts[idx] = prev_count
        prev_count += tmp
    
    ans = [-1 for i in range(len(nums)]
    for idx, n in enumerate(nums):
        ans[idx] = counts[n]
    
    return ans

"""
 [2, 2] => [0, 0]
            0  1. 2
  counts = [0, 0 ,2 ....]
  prev = 2
         0 1 2 3 4 ..
  tmp = [0 0 0 2 2.]
  
  [0, 0]
  
 
[8,1,2,2,0] => [4, 1, 2, 2, 0]

  prev_count =  4
  tmp = 2
            0  1. 2 4 5 6 7 8 
  counts = [0, 1  2         1]
                    *

         0  1. 2 4 5 6 7 8 
  tmp = [0. 1  2 4 4 4 4 4 5 5 5..]
        
ans = [4, 1, 2, 2, 0]
  
"""