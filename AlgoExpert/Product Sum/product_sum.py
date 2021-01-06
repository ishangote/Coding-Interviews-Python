# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

"""
Questions:
1. Can any special array be empty? No special array can be empty (nested or otherwise)
2. Do special arrays contain only special arrays and integers and no other data type? Yes

Examples:
input = 
[1]
ans = 1 * 1 = 1

input = 
[5, 2, [7, -1], 3, [1, [-3, 2], 4]]
                                ^
ans = 1 * (10 + 2 *(6) + 2 * (5 + 3 * (-1)))
	= 1 * (10 + 12 + 2 * (2))
	= 1 * (10 + 12 + 4)
	= 26

Recursion =>
cur_sum = 7
depth = 1

	cur_sum = 6
	depth = 2
	return 6 * 2 = 12

cur_sum = 7 + 12 = 19
depth = 1

cur_sum = 19 + 3 = 22
depth = 1

	cur_sum = 1
	depth = 2
		
		cur_sum = -1
		depth = 3
		return -1 * 3 = -3
		
	cur_sum = 2
	depth = 2
	return 2 * 2 = 4

cur_sum = 22 + 4 = 26
depth = 1
return 26 * 1 = 26

"""
def product_sum_helper(arr, depth):
	cur_sum = 0
	
	for elem in arr:
		if type(elem) == int: 
			cur_sum += elem
		else:
			cur_sum += product_sum_helper(elem, depth + 1)
			
	return cur_sum * depth
	
def productSum(array):
	return product_sum_helper(array, 1)

"""
Time: O(n), n => total number of elements in the array as well as the subarray
Space: O(d), d => maximum depth of the special array
"""