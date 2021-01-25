"""
Space optimization
"""
def nth_fibonacci_iterative_memo(n):
    if n < 1: return None
    if n == 1: return 0
    if n == 2: return 1

    prev_two = [0, 1]
    counter = 3
    while counter <= n:
        prev_two[0], prev_two[1] = prev_two[1], prev_two[0] + prev_two[1]
        counter += 1
    
    return prev_two[1]