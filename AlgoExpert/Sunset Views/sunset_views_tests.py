import unittest
from sunset_views import sunset_views

class TestSunsetViews(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs = [{"buildings": [3, 5, 4, 4, 3, 1, 3, 2],"direction": "EAST"}, {"buildings": [3, 5, 4, 4, 3, 1, 3, 2],"direction": "WEST"}, {"buildings": [10, 11],"direction": "EAST"}, {"buildings": [1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8],"direction": "WEST"}]
        self.results = [[1, 3, 6, 7], [0, 1], [1], [0, 1, 2, 4, 5, 6, 10, 13]]
    
    def test_generic(self):
        for idx, input in enumerate(self.inputs):
            self.assertEqual(self.results[idx], sunset_views(input["buildings"], input["direction"]))

if __name__ == "__main__": unittest.main()