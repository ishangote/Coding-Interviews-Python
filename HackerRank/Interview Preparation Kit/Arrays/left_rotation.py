# A left rotation operation on an array shifts each of the array's elements  unit to the left.
# Given an array  of  integers and a number, perform  left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.
"""
Questions:
1. Bounds for k? Can it be zero? Can it be greater than n? -> No, No
2. Do we have to do this inplace? -> Yes
3. Can there be duplicates? -> Yes


Examples:
[1, 2, 3, 4, 5]
d = 4
[2, 3, 4, 5, 1]
d = 3
[3, 4, 5, 1, 2]
d = 2
[4, 5, 1, 2, 3]
d = 1
[5, 1, 2, 3, 4]
d = 0

tmp = arr[0]
arr[j] = arr[j + 1] for i in range(0, n)
arr[-1] = tmp

"""
def left_rotation_arr(arr, d):
    d %= len(arr)
    for itr in range(d):
        tmp = arr[0]
        for idx in range(len(arr) - 1):
            arr[idx] = arr[idx + 1]
        arr[-1] = tmp
    return arr

"""
Time: O(d*n)
Space: O(1)
"""

"""
 0  1  2  3  4
[1, 2, 3, 4, 5]
d = 4
ans = arr[d:] + arr[:d]

 0  1  2  3  4
[1, 2, 3, 4, 5]
d = 3
ans = arr[d:] + arr[:d]
[4, 5, 1, 2, 3]

"""
def left_rotation_arr(arr, d):
    return arr[d:] + arr[:d]