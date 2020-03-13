# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. 
# If no such positive 32-bit integer exists, you need to return -1.
"""
Example 1:
Input: 12
Output: 21
 
Example 2:
Input: 21
Output: -1

I:21
O:-1

I:321
O:-1

I:4321
O:-1

I:54321
O:-1

I:987654321
O:-1

I:987654312
O:987654321


I:9 8 4 6 5 7 3 2 1
          p ^
          
  9 8 4 6 7 5 3 2 1
  
O:9 8 4 6 7 1 2 3 5

 p
12443322
     ^
13222344

1999999999
9199999999
2147483647
"""
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