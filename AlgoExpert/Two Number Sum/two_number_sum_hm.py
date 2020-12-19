"""
Examples:
arr = [2, -3, 1, 5, -1], target = 3
	   i
To find: [xi, target - xi]

hash_set =  [2, -3, 1, 5, -1]
check for target - arr[i] in hash_set


IMPORTANT TESTCASE -> 
NOT to count the same number twice, hence did not use hash_set
 0  1
[2, 3], target = 4
 i
hs = {2, 3}
output = [2, 2] -> False

{idx: num}
hash_map = {
2: 0
3: 1
}
"""
def twoNumberSumHM(array, targetSum):
    # Input validations
	if len(array) < 2: return []

	hash_map = {}
	for i in range(len(array)):
		hash_map[array[i]] = i
	
	for i in range(len(array)):
		if targetSum - array[i] in hash_map and i != hash_map[targetSum - array[i]]:
			return [array[i], targetSum - array[i]]
		
	return []
"""
Time: O(n) + O(n) ~ O(n), n = len(array)
Space: O(n) -> hash_map
"""