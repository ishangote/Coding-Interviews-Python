"""
Questions:
1. array empty? return True
2. are there duplicates? yes

Examples:
arr = 
 0  1  2   3   4  5
[2, 3, 1, -4, -4, 2]
 i
 
Pseudo:
For each idx =>
	checkby traversing arr according to rule => i += 2, i %= len(arr)
	if not check: return False
return true

Time: O(n^2)
Space: O(n)
"""
def cycle_check(idx, array, visited):
    first = idx
    while len(visited) < len(array):
        if idx in visited: return False
        visited.add(idx)
        idx = (idx + array[idx]) % len(array)
    return True if idx == first else False

def single_cycle_check(array):
    for idx in range(len(array)):
        if not cycle_check(idx, array, set()): return False
    return True