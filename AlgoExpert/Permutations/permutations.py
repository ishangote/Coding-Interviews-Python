"""
Questions:
1. Are there duplicates in array? No
2. If input empty? return empty

Examples:
         0. 1. 2. 
array = [1, 2, 3]

								     [] {1, 2, 3}
			  [1] {2, 3}			 [2]			...
	  {3}[1, 2]	 [1, 3]{2}      [2, 1]  [2, 3]
   [1, 2, 3]{}   {}[1, 3, 2] [2, 1, 3]	  [2, 3, 1]
   
Time: O(n*n!)
Space: O(n*n!)
"""
def permutations(array):
    if not array: return []
    permutations = []
    backtrack(array, [], permutations)
    return permutations

def backtrack(array, cur_permutation, permutations):
    if not array: permutations.append(cur_permutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]
            new_permutation = cur_permutation + [array[i]]
            backtrack(new_array, new_permutation, permutations)