import unittest
from balanced_brackets import balanced_brackets

class TestBalancedBrackets(unittest.TestCase):
    def setUp(self) -> None:
        self.strings = ["([])(){}(())()()", "()[]{}{", "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))", "(()())((()()()))", "((){{{{[]}}}})", "(a(", "(()agwg())((()agwga()())gawgwgag)", "aafwgaga()[]a{}{gggg"]
        self.balanced = [True, False, False, True, True, False, True, False]
    
    def test_generic(self):
        for idx, s in enumerate(self.strings):
            self.assertEqual(self.balanced[idx], balanced_brackets(s))

if __name__ == "__main__": unittest.main()