"""
Questions:
1. What if toMove is not in arr? return arr
2. In place? yes mutate the same array

Examples:

toMove = 2
arr = 
[1, 3, 4, 2, 2, 2, 2, 2]
          i
                         j

------------------------------

toMove = 2
arr = 
[1, 3, 4, 5, 5, 2, 2, 2, 2]
                i 
                           j

Time: O(n), n = len(array)
Space: O(1)
"""
def move_element_to_end(arr, to_move):
    for i in range(len(arr)):
        if arr[i] != to_move: continue
        j = i + 1

        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        
        if j == len(arr): return arr
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr