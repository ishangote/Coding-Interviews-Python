"""
Questions:
1. Are the numbers integers? yes
2. Are there duplicates in arr? yes
3. Is there only one largest range? yes assume that

Examples:
arr = [3, 5, 8, 1, 2, 4, -1, 10, 9]

Naive:
	 		 0. 1. 2. 3. 4. 5. 6. 7. 8	
sort arr = [-1, 1, 2, 3, 4, 5, 8, 9, 10]
                i
				               j				            	
idx = [1, 5]
res = [1, 5]

Time: O(nlogn)
Space:O(1)

-------------------------------------------------

Handle Duplicates? Can be removed becuase it does not affect the range
arr = 
[3, 5, 8, 1, 3, 1, 1, 2, 4, -1, 10, 9]

sort_arr = 
[-1, 1, 1, 1, 2, 3, 3, 4, 5, 8, 9, 10]

sort_set_arr = [-1, 1, 2, 3, 4, 5, 8, 9, 10]

res = [1, 5]

-------------------------------------------------
Optimization:
arr = 
[3, 5, 8, 1, 3, 1, 1, 2, 4, -1, 10, 9]
              	                    i

l = -2
h = 0
cur_length = 1
cur_range = [1, 5]

used = {
	3: F
	5: T
	8: T
	1: T
	2: T
	4: T
	-1: T
	10: T
	9: T
}

Time: O(n)
Space: O(n)
"""
def largestRangeNaive(array):
    # Handle duplicates by just removing them
    array = sorted(set(array))
    i = 0
    range_idx = [0, 0]
    while i < len(array) - 1:
        if array[i] + 1 != array[i + 1]:
            i += 1
        else:
            j = i + 1
            while j < len(array) and array[j - 1] + 1 == array[j]:
                j += 1

            if (j - 1) - i > (range_idx[1] - range_idx[0]): range_idx = [i, j - 1]

            i = j

    return [array[range_idx[0]], array[range_idx[1]]]

def largestRangeOptim(array):
    used = {}
    ans = [0, 0]
    for num in array: used[num] = False
    for num in array:
        if used[num]: continue
        cur = [0, 0]
        lo = num - 1
        hi = num + 1

        while lo in used:
            used[lo] = True
            lo -= 1
        cur[0] = lo + 1

        while hi in used:
            used[hi] = True
            hi += 1
        cur[1] = hi - 1

        if cur[1] - cur[0] >= ans[1] - ans[0]: ans = cur
    
    return ans