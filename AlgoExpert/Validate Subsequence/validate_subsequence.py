"""
Questions:
1. Duplicates? yes
2. Non contiguous? yes
3. Can there be an empty subsequence? no

Examples:
arr =
[-1, 2, 1, -3, 1, 6, 2, -7]
                            i
seq = [1, 2, -7]
                 j

arr = 
[-3, 5, 6, 1]
     i
seq = 
[5]
   j
		
"""
def isValidSubsequence(array, sequence):
    #Input Validations
	if not array or not sequence or len(sequence) > len(array): return False
	
	cur = 0
	for val in array:
		if cur == len(sequence): break
		if sequence[cur] ==  val:
			cur += 1
	
	return True if cur == len(sequence) else False

"""
Time: O(n), n is length of array
Space: O(1)
"""