"""
Questions:
1. Are the nums in array integers? Yes
2. Array never empty? No
3. Strictly increasing subsequence? Yes

Examples:
array =
 0.  1.  2.  3.  4.  5.  6. 
[10, 70, 20, 30, 50, 11, 30]
                         i
                         j
max_sums = 
  0. 1.  2.  3.  4.   5.  6. 
[10, 80, 30, 60, 110, 21, 60]
prev_idx = 
 0.    1. 2. 3. 4. 5. 6. 
[None, 0, 0, 2, 3, 0, 2]
  ^
					
max_idx = 4
max_sum = 110
subseq = 
[50, 30, 20, 10]

result = 
[110, [10, 20, 30, 50]]

-----------------------------------------

array = 
 0. 1.  2. 3. 4.  5. 6. 
[8, 12, 2, 3, 15, 5, 7]
                     i
                   j
 max_sums = 
 [8, 20, 2, 5, 35, 10, 17]
               
 prev_idx = 
  0. 1. 2. 3. 4. 5. 6.
 [N, 0, N, 2, 1, 3, 5]
              ^
subseq_indexes = 
[4, 1, 0]

Time: O(n^2)
Space: O(n)
"""

def maxSumIncreasingSubsequence(array):
    max_sums = [None] * len(array)
    prev_idx = [None] * len(array)
    max_sums[0] = array[0]

    for i in range(1, len(array)):
        max_sums[i] = array[i]
        for j in range(i):
            if array[j] < array[i]:
                if max_sums[j] + array[i] > max_sums[i]:
                    max_sums[i] = max_sums[j] + array[i]
                    prev_idx[i] = j
    
    max_sum_idx = max_sums.index(max(max_sums))

    subsequence = []
    while max_sum_idx != None:
        subsequence.append(array[max_sum_idx])
        max_sum_idx = prev_idx[max_sum_idx]
    
    return [max(max_sums), subsequence[::-1]]