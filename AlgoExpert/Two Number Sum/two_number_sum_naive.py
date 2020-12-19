"""
Questions:
1. Are there duplicates in the array? No
2. Are the numbers -+0 integers? Yes
3. Multiple answers? Return any
4. Order of ans? Any order

Examples:

arr = 
[3, 5, -4, 8, 11, 1, -1, 6],
    i
       j
target = 10

Naive: Check all pairs
"""

def twoNumberSumNaive(array, targetSum):
    #Input Validation
	if len(array) < 2: return []
	
	for i in range(len(array) - 1):
		for j in range(i + 1, len(array)):
			if array[i] + array[j] == targetSum: 
				return [array[i], array[j]]
	
	return []
"""
Time: O(n^2), n = len(arr)
Space: O(1)
"""