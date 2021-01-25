"""
Questions:
1. Is the array sorted? yes
2. How big is the input? Can lo + hi exceed sys.maxsize? Yes

Iterative Solution...
"""
def binary_search_iterative(array, target):
    lo, hi = 0, len(array) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if array[mid] == target: return mid
        if array[mid] < target: lo = mid + 1
        else: hi = mid - 1

    return -1

"""
Time: O(logn)
Space: O(1)
"""