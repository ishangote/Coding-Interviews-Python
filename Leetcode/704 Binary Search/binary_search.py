def invalid_input(items, target):
    return not items or target == None \
        or not type(target) == type(items[0]) == int \
        or not all(items[i - 1] < items[i] for i in range(1, len(items)))        

def binary_search_iterative(items, target):
    # Input validation
    if invalid_input(items, target): raise ValueError('Input not valid')

    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target: return mid
        if items[mid] < target: lo = mid + 1
        else: hi = mid - 1 
    
    return -1