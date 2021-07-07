import unittest
from task_assignment import task_assignment

class TestTaskAssignment(unittest.TestCase):
    def setUp(self) -> None:
        self.tasks = [(3, [1, 3, 5, 3, 1, 4]), (2, [1, 8, 9, 10]), (5, [3, 7, 5, 4, 4, 3, 6, 8, 3, 3])]
        self.res = [[[4, 2],[0, 5],[3, 1]], [[0, 3],[1, 2]], [[9, 7],[8, 1],[5, 6],[0, 2],[4, 3]]]

    def test_generic(self):
        for idx, (k, t) in enumerate(self.tasks):
            self.assertEqual(self.res[idx], task_assignment(k, t))

if __name__ == "__main__": unittest.main()