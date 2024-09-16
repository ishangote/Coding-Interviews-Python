# Time: O(n * r)  => n length of input_string, r => num_rows (String concatenation is expensive)
# Space: O(n)
def zigzag_conversion(input_string, num_rows):
    # Edge case
    if num_rows == 1: return input_string

    res = [[] for _ in range(num_rows)]
    level, direction = 0, "DOWN"

    for char in input_string:
        res[level].append(char)

        if level == 0: direction = "DOWN"
        if level == num_rows - 1: direction = "UP"

        level = level + 1 if direction == "DOWN" else level - 1

    ans = ''
    for levels in res:
        ans += ''.join(levels)
    
    return ans

import unittest
class TestZigZagConversion(unittest.TestCase):
    def test_zigzag_conversion_edge_case(self):
        self.assertEqual(zigzag_conversion("ABC", 1), "ABC")
        
    def test_zigzag_conversion(self):
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

if __name__ == "__main__": unittest.main()

"""
Important Edge Case

* ans += ''.join(levels) => .join() is NOT inplace operation and you need to append to ans
* initialize res = [[] for _ in range(num_rows)] => DO NOT initialize as res = [[] * num_rows]

Input:
num_rows = 1
s = 
 0
"ABC"
  ^
  * List index out of range (level = -1)

Output: "A"

Following the algorithm:
direction = "DOWN" => "UP => direction will get flipped because level == 0 and level == num_rows - 1
level = 0 => -1 => since direction gets flipped to UP level will be decremented
res = [
    [A]
]

Hence we require base case if num_rows == 1: return input_string
"""