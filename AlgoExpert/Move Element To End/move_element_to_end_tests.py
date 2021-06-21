import unittest
from move_element_to_end import move_element_to_end

class TestMoveElementToEnd(unittest.TestCase):
    def test_generic(self):
        self.assertEqual([1, 3, 4, 2, 2, 2, 2, 2], move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
        self.assertEqual([], move_element_to_end([], 3))
        self.assertEqual([1, 2, 4, 5, 6], move_element_to_end([1, 2, 4, 5, 6], 3))
        self.assertEqual([1, 2, 4, 5, 3], move_element_to_end([3, 1, 2, 4, 5], 3))

if __name__ == "__main__": unittest.main()