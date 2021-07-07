"""
Questions:
1. Duplicates? No
2. return all quads? yes
3. Any order? no

Examples:
Naive: 
Time: O(n^4)
arr = 
[7, 6, 4, -1, 1, 2]
 i
 	j
	          k
	   	         l
target = 16
res = 
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optim: Sort arr and 3 pointer with two pointers
target = 16
arr = 
[7, 6, 4, -1, 1, 2]

sort arr = 
  0. 1. 2. 3. 4. 5. 
[-1, 1, 2, 4, 6, 7]
  i
  	       j
	 	          l  h

target - (arr[i] + arr[j]) = 16 - (3) = 13

res = 
[[7, 6, 4, -1], [7, 6, 1, 2]]

Time: O(n^3)
Space: O(1)
"""

def four_sum(array, target):
    res = []
    array.sort()
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            lo, hi = j + 1, len(array) - 1
            cur_sum = target - (array[i] + array[j])
            while lo < hi:
                if array[lo] + array[hi] == cur_sum:
                    res.append([array[i], array[j], array[lo], array[hi]])
                    lo += 1
                    hi -= 1
                elif array[lo] + array[hi] < cur_sum: lo += 1
                else: hi -= 1
    
    return res