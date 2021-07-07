"""
Questions:
1. Note: building can see sunset if it is strictly taller than all of the 
buildings that come after it in the direction that it faces

Examples:
Naive: for each idx, check if idx + 1: end are smaller
Time: O(n^2)
Space: O(1)

Keep track of max_height so far from the reverse side:
direction = "EAST"
buildings = 
 0. 1. 2. 3. 4. 5. 6. 7.
[3, 5, 4, 4, 3, 1, 3, 2]
 ^
max_height = 5
ans = [7, 6, 3, 1]
return ans[::-1]

Time: O(n)
Space: O(1)
"""

def sunset_views(buildings, direction):
    if direction == "EAST": start, end, step = len(buildings) - 1, -1, -1
    else: start, end, step = 0, len(buildings), 1

    res = []
    max_height = 0
    for idx in range(start, end, step):
        if buildings[idx] > max_height:
            res.append(idx)
            max_height = buildings[idx]
    
    return res if direction == "WEST" else res[::-1]