"""
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
 
 
 i -> row
 j -> col
 i + 1
 j + 1
 
 
  0 1 2
      
0 1 2 3
1 5 1 2
2 4 5 1

Time Complextiy: O(n)
Space Complexity: O(1)
 
"""
def isToeplitz(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr[0]) - 1):

      if arr[i][j] != arr[i + 1][j + 1]: return False

  return True

import unittest
class TestToeplitz(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(isToeplitz([[4,0],[9,4]]), True)
        self.assertEqual(isToeplitz([[6,4,4]]), True)
        self.assertEqual(isToeplitz([[3],[5],[6]]), True)
        self.assertEqual(isToeplitz([[3,9],[5,3],[6,5]]), True)
        self.assertEqual(isToeplitz([[3,1,7],[4,1,1],[2,4,3]]), False)
        self.assertEqual(isToeplitz([[8,8,8,8,8],[8,8,8,8,9],[8,8,8,8,8],[8,8,8,8,8],[8,8,8,8,8]]), False)

if __name__ == "__main__": unittest.main()