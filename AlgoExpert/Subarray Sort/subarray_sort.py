"""
Questions:
1. Are there duplicates? yes
2. What if arr is sorted? return [-1, -1]

Examples:
array = 
 0. 1. 2. 3. 4.  5.
[1, 2, 3, 4, 5, -1]
res = [0, 5]

out of place elements = {5, -1}

array = 
 0. 1.  2. 3. 4. 5.
[9, 1,  2, 3, 4, 5]
res = [0, 5]

out of place elements = {9, 1}

array = 
 0. 1. 2. 3. 4. 
[3, 4, 2, 1, 5]

out of place elements = {4, 2, 1}

res = [0, 3]

left bound of subarray decided by smallest out of place element and right bound of subarray is 
decided by largest out of place element

array = 
 0. 1. 2. 3. 4.  5.  6. 7.  8. 9. 10. 11. 12. 
[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
                               i
out_of_place_elements = {11, 7, 12, 6}
min_elem = 6
max_elem = 12

find lower bound to put min_elem at and find higher bound to put 12 at
                            
array = 
 0. 1. 2. 3. 4.  5.  6. 7.  8. 9. 10. 11. 12. 
[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
          i
		  >6
		  
array = 
 0. 1. 2. 3. 4.  5.  6. 7.  8. 9. 10. 11. 12. 
[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
          					   i
							   <12

res = [3, 9]
"""
def get_out_of_order_elememts(array):
    out_of_order_elements = set()
    for i in range(len(array)):
        if i == 0:
            if array[i] > array[i + 1]: out_of_order_elements.add(array[i])

        elif i == len(array) - 1:
            if array[i - 1] > array[i]: out_of_order_elements.add(array[i])

        else:
            if array[i - 1] <= array[i] <= array[i + 1]: continue
            out_of_order_elements.add(array[i])

    return out_of_order_elements
            
def subarray_sort(array):
    res = [-1, -1]
    out_of_order_elements = get_out_of_order_elememts(array)
    if not out_of_order_elements: return res

    min_element = min(out_of_order_elements)
    max_element = max(out_of_order_elements)

    for i in range(len(array)):
        if array[i] > min_element: 
            res[0] = i
            break
    
    for i in range(len(array) - 1, -1, -1):
        if array[i] < max_element: 
            res[1] = i
            break
    
    return res