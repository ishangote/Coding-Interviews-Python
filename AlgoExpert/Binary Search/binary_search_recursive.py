"""
Recursive solution
"""
def binary_search_recursive_helper(arr, target, lo, hi):
    if lo > hi: return -1
    mid = lo + (hi - lo) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target: return binary_search_recursive_helper(arr, target, mid + 1, hi)
    return binary_search_recursive_helper(arr, target, lo, mid - 1)
	
def binary_search_recursive(array, target):
    return binary_search_recursive_helper(array, target, 0, len(array) - 1)

"""
Time: O(logn)
Space: O(1) ?
"""