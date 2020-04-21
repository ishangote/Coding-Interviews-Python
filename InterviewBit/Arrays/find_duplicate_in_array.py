"""
Input:
  0 1  2  3 4
[-3 4 -1 -4 1]
          ^
      
abs(v) - 1

Pseudo: 
val in arr:
    if arr[abs(val) - 1] < 0: return abs(val)
    arr[abs(val) - 1] *= -1
    
return -1


Output:
1

Input:
 0 1 2 3 4
[3 1 2 4 5]

Output:
-1
"""
def repeatedNumber(A):
    if not A: return -1
    A = list(A)
    for val in A:
        if A[abs(val) - 1] < 0: return abs(val)
        A[abs(val) - 1] *= -1
        
    return -1

import unittest
class TestFindDuplicateInArray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(repeatedNumber([3, 4, 1, 4, 1]), 4)
        self.assertEqual(repeatedNumber([3, 5, 2, 4, 1]), -1)

if __name__ == "__main__": unittest.main()