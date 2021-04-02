"""
Examples:
A =
[5, 7, 8, 9, 7, 9, 9]
 ^
nums = {5, 7, 8, 9}
dups = {7, 9}
unique_nums = nums - dups = {5, 8}
ans = 8
"""

"""
Time: O(n)
Space: O(n)
"""

def largest_unique_number_optim(A):
    nums = set()
    dups = set()
    for num in A:
        if num in nums:
            dups.add(num)
        else:
            nums.add(num)
    
    unique_nums = nums - dups
    if unique_nums: return max(unique_nums)
    return -1