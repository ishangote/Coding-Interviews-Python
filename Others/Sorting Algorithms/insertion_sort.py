"""
Insertion Sort:
input = 
[8, 5, 2, 9, 5, 6, 3]
	s
 e

[5, 8, 2, 9, 5, 6, 3]
	   s
    e
	
[2, 5, 8, 9, 5, 6, 3]
	         s
          e
          j
	   
[2, 5, 5, 8, 9, 6, 3]
	            s
             e
    j
	
[2, 5, 5, 6, 8, 9, 3]
	               s
                e
       j
	   
[2, 3, 5, 5, 6, 8, 9]
	                  s
                   e
 				   j

e -> pointer points to the end of sorted array
s -> pointer points to the start of unsorted array and 

"""
import time
def insertionSort(array):
    start = time.time()

    for e in range(len(array) - 1):
        if array[e] <= array[e + 1]: continue
        j = e
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1

    end = time.time()
    print(f"Runtime of Insertion sort is {end - start}")

    return array

"""
Time: O(n^2), n => length of input array
Space: O(1)
"""
			
"""
Testcase
INPUT						EXPECTED				ACTUAL
 0   1   2
[3, -1, -2]					[-2, -1, 3]				[-2, -1, 3]

[]							[]						[]

[1]							[1]						[1]
 
"""