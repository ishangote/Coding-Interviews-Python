"""
Questions:
1. Empty array? Monotonic

Time: O(n), n => number of elements in arr
Space: O(1)
"""

def check_increasing(arr):
	for i in range(1, len(arr)):
		if arr[i - 1] > arr[i]: return False
	return True
		
def check_decreasing(arr):
	for i in range(1, len(arr)):
		if arr[i - 1] < arr[i]: return False
	return True
	
def isMonotonic(array):
	return check_increasing(array) or check_decreasing(array)