import unittest
from valid_starting_city import valid_starting_city_naive

class TestValidStartingCity_naive(unittest.TestCase):
    def setUp(self):
        self.tests = [{"distances": [5, 25, 15, 10, 15], "fuel": [1, 2, 1, 0, 3], "mpg": 10, "ans": 4}, {"distances": [10, 20, 10, 15, 5, 15, 25], "fuel": [0, 2, 1, 0, 0, 1, 1], "mpg": 20, "ans": 1}, {"distances": [30, 25, 5, 100, 40], "fuel": [3, 2, 1, 0, 4], "mpg": 20, "ans": 4}, {"distances": [5, 2, 3], "fuel": [1, 0, 1], "mpg": 5, "ans": 2}]
    
    def test_brute_force(self):
        for test in self.tests:
            self.assertEqual(test["ans"], valid_starting_city_naive(test["distances"], test["fuel"], test["mpg"]))

if __name__ == "__main__": unittest.main()