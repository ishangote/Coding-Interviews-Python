"""
Examples:
arr = 
[12, 3, 1, 2, -6, 5, -8, 6]
target = 0
output = 
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

----------------------
Two Pointers Solution
sort the array ->

[-8, -6, 1, 2, 3, 5, 6, 12]
                  i
  	     l					
	  		      h
CASE1:
arr[i] + arr[l] + arr[h] < targetSum
arr[i] + arr[l] + arr[h] > targetSum
WE MUST MOVE either lo or hi but not both

CASE2:
arr[i] + arr[l] + arr[h] == targetSum
WE MUST MOVE lo and hi both because we do not know if we want to increase the cur sum or decrease it

output = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

def three_sum_two_pointers(array, target):
    if len(array) < 3: return []
    array = sorted(array)
    output = []

    for idx in range(len(array) - 2):
        lo, hi = idx + 1, len(array) - 1
        while lo < hi:
            if array[idx] + array[lo] + array[hi] < target:
                lo += 1
            elif array[idx] + array[lo] + array[hi] > target:
                hi -= 1
            else:
                output.append([array[idx], array[lo], array[hi]])
                lo += 1
                hi -= 1
            
    return output