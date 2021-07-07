
"""
Questions:
1. if input is empty? yes
2. duplicates/-ve nos? yes
3. subarray -> contiguous
4. subarray size 1

number of subarrays: n(n+1)/2

Examples:
array = 
[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
max_sums = 
[3, 8, -1, 1, 4, 2, 5, 9, 16 18, 9, 15, 18, 19, 14, 18]
"""
# Time: O(n^2)
# Space: O(n^2)
import sys
def naive(array):
    subarrays = []
    for i in range(len(array) + 1):
        for j in range(i):
            subarrays.append(array[j:i])
    
    max_sum = -sys.maxsize
    for subarr in subarrays:
        max_sum = max(max_sum, sum(subarr))
    
    return max_sum

# Time: O(n)
# Space: O(n)
def kadane_optim(array):
    max_sums = [0] * len(array)
    max_sums[0] = array[0]

    for i in range(1, len(array)):
        max_sums[i] = max(max_sums[i - 1] + array[i], array[i])
    
    return max(max_sums)

# Time: O(n)
# Space: O(1)
def kadane_space_optim(array):
    max_sum = prev_sum = array[0]
    
    for i in range(1, len(array)):
        prev_sum = max(prev_sum + array[i], array[i])
        max_sum = max(prev_sum, max_sum)
    
    return max(max_sum, prev_sum)