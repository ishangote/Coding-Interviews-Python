# https://leetcode.com/problems/next-greater-element-iii/ On Leetcode

def next_greater_element_iii(n):
    #In Python strings are immutable. You can't modify them. Hence list
    n = list(str(n))
    
    idx = len(n) - 1
    while idx > 0 and n[idx - 1] >= n[idx]:
        idx -= 1
    
    if idx == 0: return -1
    
    pivot = idx - 1
            
    idx = len(n) - 1
    while n[idx] <= n[pivot]:
        idx -= 1
        
    swap(n, pivot, idx)
    reverse(n, pivot + 1, len(n) - 1)

    ans = int(''.join(n))
    return ans if ans <= 2 ** 31 - 1 else -1

def reverse(n, i, j):
    while i < j:
        swap(n, i, j)
        i += 1
        j -= 1

def swap(n, i, j):
    n[i], n[j] = n[j], n[i]

import unittest
class TestNextGreaterElementIII(unittest.TestCase):
    def test_next_greater_element(self):
        self.assertEqual(next_greater_element_iii(12), 21)
        self.assertEqual(next_greater_element_iii(21), -1)
        self.assertEqual(next_greater_element_iii(12443322), 13222344)
        self.assertEqual(next_greater_element_iii(1999999999), -1)

if __name__ == "__main__": unittest.main()

"""
Feedback:
Good, short intro
Did not write what's input and output.
12
21

Again horizontal writing for phone interview

Took small example
Took sorted example 1, 2, 3 in sequence instead of a random enough value

Took 10, 20 and ->
"Any number which is divisible by 10 shoud output none"  ---> HARD REJECT --> non-logical conclusions
After pointing out -> I need to take more examples, but no taking back of the previous statement --> RED FLAG

Lot of breaks while talking

Did not get hint to not use SET
Kept optimizing for 2*O(N) -->> Straight reject, basic Big O not clear

Said "..where n is number of digits we have traversed till now" --> Big O is worst case, n should be total number of digts

if input[idx] > input[idx - 1]:
Always write condition in INDEX ORDER to avoid confusions; if input[idx - 1] < input[idx]:
"""