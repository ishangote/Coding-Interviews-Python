import unittest
from product_sum import productSum

class TestProductSum(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]), 12)
        self.assertEqual(productSum([[1, 2], 3, [4, 5]]), 27)
        self.assertEqual(productSum([[[[[5]]]]]), 600)

if __name__ == "__main__": unittest.main()