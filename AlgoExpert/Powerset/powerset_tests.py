import unittest
from powerset import powerset_iterative, powerset_recursive

class TestPowerset(unittest.TestCase):
    def setUp(self):
        self.tests = [{"nums": [1, 2], "ans": [[], [1], [2], [1, 2]]}, {"nums": [1, 2, 3], "ans": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]}]
    
    def test_iterative(self):
        for test in self.tests:
            self.assertListEqual(test["ans"], powerset_iterative(test["nums"]))
    
    def test_recursive(self):
        for test in self.tests:
            self.assertListEqual(test["ans"], powerset_recursive(test["nums"]))
    
if __name__ == "__main__": unittest.main()