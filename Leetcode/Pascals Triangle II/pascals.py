

"""
     1              k = 0
    1 1             k = 1
   1 2 1            k = 2
  1 3 3 1           k = 3
 1 4 6 4 1          k = 4
"""
import unittest
def pascals(k):
    if k == 0: return [1]
    if k == 1: return [1, 1]
    return pascals_helper(pascals(k - 1))

def pascals_helper(prev_row):
    result = []
    result.append(1)
    i, j = 0, 1
    while j < len(prev_row):
        result.append(prev_row[i] + prev_row[j])
        j += 1
        i += 1
    result.append(1)
    return result

class TestPascals(unittest.TestCase):
    def test_k_0_1(self):
        self.assertEqual(pascals(0), [1])
        self.assertEqual(pascals(1), [1, 1])

    def test_pascals_k(self):
        self.assertEqual(pascals(2), [1, 2, 1])
        self.assertEqual(pascals(3), [1, 3, 3, 1])
        self.assertEqual(pascals(4), [1, 4, 6, 4, 1])
        

if __name__ == "__main__": unittest.main()