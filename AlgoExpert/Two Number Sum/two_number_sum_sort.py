"""
Examples:
arr = [2, -3, 1, 5, -1], target = 3

sort =>
arr =
[-3, -1, 1, 2, 5]
         l			   
			r
"""

def twoNumberSumSort(array, targetSum):
    #Input validations
	if len(array) < 2: return []
	array.sort()
	lo, hi = 0, len(array) - 1
	
	while lo < hi:
		cur_sum = array[lo] + array[hi]
		if cur_sum == targetSum: return [array[lo], array[hi]]
		if cur_sum < targetSum: lo += 1
		else: hi -= 1
	
	return []
"""
Time: O(nlogn), n = len(arr)
Space: O(1) {O(n) -> internally python uses tim sort}
"""