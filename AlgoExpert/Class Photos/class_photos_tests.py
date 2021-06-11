import unittest
from class_photos import class_photos

class TestClassPhotos(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(True, class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
        self.assertEqual(True, class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
        self.assertEqual(False, class_photos([6], [6]))
        self.assertEqual(False, class_photos([5, 6, 7, 2, 3, 1, 2, 3], [1, 1, 1, 1, 1, 1, 1, 1]))

if __name__ == "__main__": unittest.main()