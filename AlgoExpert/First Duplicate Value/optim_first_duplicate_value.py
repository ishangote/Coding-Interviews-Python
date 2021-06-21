"""
Questions:
1. What if no duplicate num? return -1
2. More than 1 duplicate numbers? return first integer that is duplicate
3. Are any numbers -ve? No
4. Array can be mutated? NO

NOTE: Arrray needs to be mutable!

Examples:
arr = 
 0   1   2   3  4   5  6		     0. 1. 2. 3. 4. 5. 6.
[2, -1, -5, -3, 3, -2, 4] 			{1, 2, 3, 4, 5, 6, 7}
                i
 
 2%7 = 2
 1%7 = 1
 5%7 = 5
 3%7 = 3

if num at abs(arr[i]) % len(arr) < 0: return abs(arr[i])
else: num at abs(arr[i] % len(arr)) *= -1

Time: O(n)
Space: O(1)
"""
def optim_first_duplicate_val(array):
    for idx, val in enumerate(array):
        if array[abs(array[idx]) % len(array)] < 0: return abs(array[idx])
        array[abs(array[idx]) % len(array)] *= -1
    return -1    