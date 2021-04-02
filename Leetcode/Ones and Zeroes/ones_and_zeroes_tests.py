import unittest
from ones_and_zeroes import ones_and_zeroes_naive
from ones_and_zeroes_memo import ones_and_zeroes_memo

class TestOnesAndZeroes(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(4, ones_and_zeroes_naive(["10","0001","111001","1","0"], 5, 3))
        self.assertEqual(2, ones_and_zeroes_naive(["10","0","1"], 1, 1))
    
    def test_memo(self):
        self.assertEqual(4, ones_and_zeroes_memo(["10","0001","111001","1","0"], 5, 3))
        self.assertEqual(2, ones_and_zeroes_memo(["10","0","1"], 1, 1))
        

if __name__ == "__main__": unittest.main()