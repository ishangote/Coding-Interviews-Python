"""
Memoization:

store (idx, m, n) tuple in hash map
"""

def get_counts(s):
    zeroes, ones = 0, 0
    for num in s:
        if num == "0": zeroes += 1
        else: ones += 1
    return [zeroes, ones]

def ones_and_zeroes_memo(strs, m, n):
    return ones_zeroes_helper(strs, m, n, 0, {})

def ones_zeroes_helper(strs, zeroes, ones, idx, memo):
    #Break condition
    if idx == len(strs) or zeroes + ones == 0: return 0
    if (idx, zeroes, ones) in memo: return memo[(idx, zeroes, ones)]
    
    count0, count1 = get_counts(strs[idx])
    accept = 0
    if count0 <= zeroes and count1 <= ones:
        accept = 1 + ones_zeroes_helper(strs, zeroes - count0, ones - count1, idx + 1, memo)
    
    reject = ones_zeroes_helper(strs, zeroes, ones, idx + 1, memo)
    
    memo[(idx, zeroes, ones)] = max(accept, reject)
    return memo[(idx, zeroes, ones)]