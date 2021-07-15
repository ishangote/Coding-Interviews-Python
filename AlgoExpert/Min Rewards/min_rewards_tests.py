import unittest
from min_rewards import minRewards

class TestMinRewards(unittest.TestCase):
    def setUp(self) -> None:
        self.scores = [[8, 4, 2, 1, 3, 6, 7, 9, 5], [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0], [1], [800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53], [4, 2, 1, 3]]
        self.min_rewards = [25, 52, 1, 93, 8]
        return super().setUp()
    
    def test_generic(self):
        for idx in range(len(self.scores)):
            self.assertEqual(self.min_rewards[idx], minRewards(self.scores[idx]))

if __name__ == "__main__": unittest.main()