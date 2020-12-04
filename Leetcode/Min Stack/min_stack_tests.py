import unittest
from min_stack import MinStack
class TestMinStack(unittest.TestCase):
    def test_generic(self):
        min_stack = MinStack()
        self.assertEqual(min_stack.push(3), None)
        self.assertEqual(min_stack.push(4), None)
        self.assertEqual(min_stack.push(1), None)
        self.assertEqual(min_stack.push(5), None)

        self.assertEqual(min_stack.getMin(), 1)
        self.assertEqual(min_stack.pop(), 5)

if __name__ == "__main__": unittest.main()