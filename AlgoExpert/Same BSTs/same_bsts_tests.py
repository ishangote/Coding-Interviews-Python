import unittest
from same_bsts import same_bsts

class TestSameBSTs(unittest.TestCase):
    def setUp(self) -> None:
        self.arrayOnes = [[7, 6, 5, 4, 3, 2, 1], [10, 15, 8, 12, 94, 81, 5, 2, -1, 101, 45, 12, 8, -1, 8, 2, -34], [50, 76, 81, 23, 23, 23, 100, 56, 12, -1, 3], [10, 15, 8, 12, 94, 81, 5, 2, 11]]
        self.arrayTwos = [[7, 6, 5, 4, 3, 2, 1, 0], [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 8, 12, 45, 100], [50, 23, 76, 23, 23, 12, 56, 81, -1, 3, 100], [10, 8, 5, 15, 2, 12, 11, 94, 81]]
        self.areSame = [False, False, True, True]
        return super().setUp()
    
    def test_generic(self):
        for idx in range(len(self.arrayOnes)):
            self.assertEqual(self.areSame[idx], same_bsts(self.arrayOnes[idx], self.arrayTwos[idx]))
    
if __name__ == "__main__": unittest.main()