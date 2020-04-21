"""
1 2
3 4
 
Transpose = 
1 3
2 4
 
Reverse Rows =
3 1
4 2
 
Input = 
1 3 2
4 3 6
2 1 7
 
Transpose = 
1 4 2
3 3 1
2 6 7
 
Reverse Rows = 
2 4 1
1 3 3
7 6 2
 
"""
def rotate(A):
    if not A: return A
    
    #Transpose
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    
    for row in A:
        row.reverse()

    return A

import unittest
class TestRotateMatrix(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(rotate([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

if __name__ == "__main__": unittest.main()