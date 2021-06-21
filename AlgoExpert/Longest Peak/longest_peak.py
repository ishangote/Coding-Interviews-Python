"""
Questions:
1. arr montonic? 
2. len(arr) < 3? No

Examples:
[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

peaks = {4, 10}

peak 4:
[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
                i	              
				   j

length = 1

Time: O(n), n is num of elements in arr
Space: O(1)	   
"""
import sys
def longest_peak(array):
    peaks = []
    for idx in range(1, len(array) - 1):
        if array[idx - 1] < array[idx] > array[idx + 1]: peaks.append(idx)
    
    max_len = 0
    for p in peaks:
        i, j = p, p
        p_len = 1
        
        while i > 0 and array[i - 1] < array[i]:
            i -= 1
            p_len += 1
        
        while j < len(array) - 1 and array[j] > array[j + 1]:
            j += 1
            p_len += 1
        
        if p_len > max_len: max_len = p_len
    
    return max_len