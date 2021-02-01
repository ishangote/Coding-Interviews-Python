import unittest
from smalest_difference import smallest_difference_optim

class TestSmallestDifference(unittest.TestCase):
    algo_tests = []
    
    def setUp(self) -> None:
        self.algo_tests = [[[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]], [[-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]], [[10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [1000, 1014]], [[10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [530, 530]]]
        return super().setUp()

    def test_algo_expert_testcases(self):
        for test in self.algo_tests:
            arr1 = test[0]
            arr2 = test[1]
            expected_ans = test[2]
            self.assertEqual(expected_ans, smallest_difference_optim(arr1, arr2))

if __name__ == "__main__": unittest.main()