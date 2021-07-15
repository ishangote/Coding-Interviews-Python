"""
Questions:
1. Are all integers in arrays? Yes
2. arr1 == arr2 == None? return True

Examples:
bst = 
			10
		8		15
      5		 12    94
    2		11	 81
	
arr1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arr2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
		^	

Two subtree BSTs
		SUB1	SUB2
		8		15
      5		 12    94
    2		11	 81

arr1 = [15, 8, 12, 94, 81, 5, 2, 11]
		 *  ^	*	*  *   ^  ^  *
	   [8, 5, 2] => Represents arr1_SUB1
	   [15, 12, 94, 81, 11] => Represents arr1_SUB2
	   
arr2 = [8, 5, 15, 2, 12, 11, 94, 81]
		^  ^  *   ^  *   *   *   *
	   [8, 5, 2] => Represents arr2_SUB1
	   [15, 12, 11, 94, 81] => Represents arr2_SUB2

return same_bst(arr1_sub1, arr2_sub1) and same_bst(arr1_sub2, arr2_sub2)
Base Condition
if not arr1 and not arr2: return True
if len(arr1) != len(arr2) or arr1[0] != arr2[0]: return False
"""

def same_bsts(arr1, arr2):
    if arr1 == arr2: return True
    if len(arr1) != len(arr2): return False
    if arr1[0] != arr2[0]: return False

    root_val = arr1[0]
    left_subtree_1 = [val for val in arr1[1: ] if val < root_val]
    right_subtree_1 = [val for val in arr1[1: ] if val >= root_val]

    left_subtree_2 = [val for val in arr2[1: ] if val < root_val]
    right_subtree_2 = [val for val in arr2[1: ] if val >= root_val]

    return same_bsts(left_subtree_1, left_subtree_2) and same_bsts(right_subtree_1, right_subtree_2)