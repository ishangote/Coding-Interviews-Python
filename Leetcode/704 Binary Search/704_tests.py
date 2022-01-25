import unittest
from binary_search import binary_search_iterative

class TestBinarySearch(unittest.TestCase):
    def test_input_validation(self):
        with self.assertRaises(ValueError): binary_search_iterative([], 2)
        with self.assertRaises(ValueError): binary_search_iterative([1, 2], None)
        with self.assertRaises(ValueError): binary_search_iterative(['a', 'b'], 'b')
        with self.assertRaises(ValueError): binary_search_iterative([], None)
        with self.assertRaises(ValueError): binary_search_iterative([1, 2, 3, 3, -1, 2], 2)
    
    def test_target_not_in_items(self):
        self.assertEqual(binary_search_iterative([-1, 4, 5, 11, 18, 23], 6), -1)
        self.assertEqual(binary_search_iterative([-19, -13, 0, 1, 2], -2), -1)
    
    def test_target_in_items(self):
        self.assertEqual(binary_search_iterative([-1, 4, 5, 11, 18, 23], 4), 1)
        self.assertEqual(binary_search_iterative([-19, -13, 0, 1, 2], 1), 3)
    
    def test_edge_locations(self):
        self.assertEqual(binary_search_iterative([-12, 3, 5, 8], 8), 3)
        self.assertEqual(binary_search_iterative([-12, 3, 5, 8], -12), 0)
            

if __name__ == '__main__': unittest.main()