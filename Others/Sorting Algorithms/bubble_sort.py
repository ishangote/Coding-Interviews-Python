"""
Bubble Sort
[8, 5, 2, 9, 5, 6, 3]
iteration 1
[5, 2, 8, 5, 6, 3, 9]
                   i
iteration 2
[2, 5, 5, 6, 3, 8, 9]
                   i
				   
iteration 3
[2, 5, 5, 3, 6, 8, 9]
                   i
				   
iteration 4
[2, 5, 3, 5, 6, 8, 9]
                    i
					
iteration 5
[2, 3, 5, 5, 6, 8, 9]
                   i
				   
iteration 6
[2, 3, 5, 5, 6, 8, 9]

No swap => return array
"""
import time
def bubbleSort(array):
    start = time.time()

    swap_flag = True
    while swap_flag:
        swap_flag = False
        for idx in range(len(array) - 1):
            if array[idx] <= array[idx + 1]: continue
            array[idx], array[idx + 1] = array[idx + 1], array[idx]
            swap_flag = True
	
    end = time.time()
    print(f"Runtime of Bubble sort is {end - start}")

    return array

"""
Time: O(n^2), n => length of array
Space: O(1)
"""