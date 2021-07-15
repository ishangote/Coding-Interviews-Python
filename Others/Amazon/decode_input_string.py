# Decode the input string into original string.
# You are given an encoded string  and number of rows, Convert it to original string
  
# Input: mnesi___ya__k____mime  N = 3
# Output : my name is mike
# Explanation : Read the matrix in a diagonal way starting from [0][0] index until the end of row and start from the top
# again to decode it. _ are treated as space.


"""
Example 1:

n = 3
input_string = 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
m n e s i _ _ _ y a _  _  k  _  _  _  _  m  i  m  e


len(s) = 21
chars/row = 21/ 3 = 7
matrix = [
          0 1 2 3 4 5 6
       0 [m n e s i _ _],
       1 [_ y a _ _ k _],
       2 [_ _ _ m i m e]
    ]

ans = 
"my_name_is_mike___"

"""
def build_matrix(input_string, mat_size):
    matrix = []
    num_chars_per_row = len(input_string) // mat_size
    
    for i in range(0, len(input_string), num_chars_per_row):
        row = list(input_string[i:i + num_chars_per_row])
        matrix.append(row)
    
    return matrix

# Question: Are the leading spaces in the output to be removed?
def decode_input_string(input_string, mat_size):
    # Input Validations...
    if not input_string: return ""

    matrix = build_matrix(input_string, mat_size)
    ans = []
    for i in range(len(matrix[0])):
        row, col = 0, i
        while row < len(matrix) and col < len(matrix[0]):
            if matrix[row][col] == '_':
                ans.append(' ')
            else: 
                ans.append(matrix[row][col])
            row += 1
            col += 1
    
    return ''.join(ans)

import unittest
class TestDecodeString(unittest.TestCase):
    def test_generic(self):
        self.assertEqual("my name is mike   ", decode_input_string("mnesi___ya__k____mime", 3))

if __name__ == "__main__": unittest.main()