"""
SUBSTRING: CONTIGUOUS!
Brute Force:
Time: O(n^3)
Space: O(1)


0 1 2 3 4 5 6 7 8
x a x b b x a c x
i 
              j

max_len = 

"""
def get_palin_len(s, i, j):
    if i < 0 or j >= len(s) or s[i] != s[j]: return 0
    
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    
    return j - i - 1

def longest_palin(s):
    #Input validations
    if len(s) == 0 or len(s) == 1: return len(s)

    max_len = 0
    for i in range(len(s) - 1):
        even_palin_len = get_palin_len(s, i, i + 1)
        odd_palin_len = get_palin_len(s, i, i)
        max_len = max(max_len, even_palin_len, odd_palin_len)
    
    return max_len

"""
In                      Expected                  Actual
''                      0                         0
'a'                     1                         1

'ab'                    1                         1


012345678
xaxbbxacx               6                         6
  ^

i = -1
j = 3

max_len = 3


"""