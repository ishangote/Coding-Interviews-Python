"""
Examples:
arr = 
[12, 3, 1, 2, -6, 5, -8, 6]
target = 0
output = 
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

----------------------
Hash Map Solution
sort the input ->

a + b + c = target
a + (target - a) = target

  0   1  2  3  4  5  6  7
[-8, -6, 1, 2, 3, 5, 6, 12]
  i 
                  j 
				  
DO NOT WANT TO ADD [-8, 5, 3] to the output -> 
check if hm[target - sum(i, j)] > j only then add to output

14
nums_hash_map = {
	-8: 0
	-6: 1
	1: 2
	2: 3
	3: 4
	5: 5
	6: 6
	12: 7
}

output = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""
def three_sum_hm(array, target):

    #Remember to sort for output format
    array = sorted(array)
    num_to_idx = {}
    for idx in range(len(array)):
        num_to_idx[array[idx]] = idx

    output = []
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            if target - array[i] - array[j] in num_to_idx and num_to_idx[target - array[i] - array[j]] > j:
                output.append([array[i], array[j], target - array[i] - array[j]])

    return output

"""
Time: O(nlogn) + O(n^2) ~ O(n^2), n -> count of numbers in array
Space: O(n) 
"""