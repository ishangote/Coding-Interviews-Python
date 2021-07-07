import unittest
from sort_stack import sort_stack

class TestSortStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stacks = [[-5, 2, -2, 4, 3, 1], [3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3], [], [3, 3, 3, 3, 3, 3], [2, 4, 22, 1, -9, 0, 6, 23, -2, 1]]
        self.sorted_stacks = [[-5, -2, 1, 2, 3, 4], [-1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5], [], [3, 3, 3, 3, 3, 3], [-9, -2, 0, 1, 1, 2, 4, 6, 22, 23]]
    
    def test_generic(self):
        for idx, stack in enumerate(self.stacks):
            self.assertEqual(self.sorted_stacks[idx], sort_stack(stack))

if __name__ == "__main__": unittest.main()