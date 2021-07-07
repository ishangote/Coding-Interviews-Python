"""
Questions:
1. if input empty? return 0
2. Can there be -ve nos? No
3. Duplicates? yes?
4. input mutable? yes

Examples:
	 0  1   2   3  4  5
	[7, 10, 12, 7, 9, 14]
	                  ^
inc	 7  10  19  17 18 33
exc  0  7   10  19 19 19

return 33

Time: O(n)
Space: O(n)
"""

def max_sum_naive(array):
    if not array: return 0
    inc, exc = [0] * len(array), [0] * len(array)

    inc[0] = array[0]

    for idx in range(1, len(array)):
        inc[idx] = array[idx] + exc[idx - 1]
        exc[idx] = max(inc[idx - 1], exc[idx - 1])

    return max(exc[-1], inc[-1])

def max_sum_optim(array):
    if not array: return 0
    prev_inc, prev_exc = array[0], 0

    for idx in range(1, len(array)):
        prev_exc, prev_inc = max(prev_inc, prev_exc), prev_exc + array[idx]

    return max(prev_inc, prev_exc)