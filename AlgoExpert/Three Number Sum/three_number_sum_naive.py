"""
Questions:
1. Are there duplicates in the array? No
2. len(array) < 3: return []
3. What if there are multiple solutions? return all triplets
4. Order of output? Return triplets sorted 

Examples:
arr = 
[12, 3, 1, 2, -6, 5, -8, 6]
target = 0

sorted ->
[-8, -6, 1, 2, 3, 5, 6, 12]
  i
      j  
               k  

Naive Approach:
1. Sort the array
2. Loop over array thrice (i, j, k)

"""
def three_sum_naive(array, target):
    if len(array) < 3: return []
    array = sorted(array)

    output = []

    for i in range(0, len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == target: 
                    output.append([array[i], array[j], array[k]])
    return output

"""
Time: O(n^3)
Space: O(n)
"""