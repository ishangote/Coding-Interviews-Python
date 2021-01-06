"""
Selection Sort

Example:
arr = 
[8, 5, 2, 9, 5, 6, 3]
output =
[2, 3, 5, 5, 6, 8, 9]

s -> pointer points to start of the unsorted part (init = 0)
m -> poniter points to the current min number in the unsorted part
i -> runner pointer on the unsorted part

[8, 5, 2, 9, 5, 6, 3]
 s
 m
    i 
					 
[2, 5, 8, 9, 5, 6, 3]
    s
    			   m
                     i
					 
[2, 3, 8, 9, 5, 6, 5]
       s
             m
                     i
					 
[2, 3, 5, 9, 8, 6, 5]
          s
                   m
		              i

[2, 3, 5, 5, 8, 6, 9]
             s
                m
			          i
					  
[2, 3, 5, 5, 6, 8, 9]
                s
                m
		             i
					 
[2, 3, 5, 5, 6, 8, 9]
                   s
                   m
  		           	  i

"""
import time
def selectionSort(array):
    start = time.time()

    for s in range(len(array) - 1):
        cur_min_pointer = s

        for i in range(s + 1, len(array)):
            if array[i] < array[cur_min_pointer]: cur_min_pointer = i

        array[s], array[cur_min_pointer] = array[cur_min_pointer], array[s]

    end = time.time()
    print(f"Runtime of Selection sort is {end - start}")

    return array

"""
Time: O(n^2), n => length of the input array
Space: O(1)
"""

"""
Testcases:
INPUT					EXPECTED				ACTUAL
[]						[]						[]
[1]						[1]						[1]

[3, -1, -2]				[-2, -1, 3]				[-2, -1, 3]

"""