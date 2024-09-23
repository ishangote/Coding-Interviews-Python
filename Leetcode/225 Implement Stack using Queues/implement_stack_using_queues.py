import unittest
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    # Time: O(n), where n => size of the stack
    def push(self, value):
        self.q2.appendleft(value)

        while self.q1:
            self.q2.appendleft(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1

    # Time: O(1)
    def pop(self):
        return self.q1.pop()

    # Time: O(1)
    def top(self):
        return self.q1[-1]

    # Time: O(1)
    def empty(self):
        return len(self.q1) == 0


class TestMyStack(unittest.TestCase):
    def test_my_stack(self):
        my_stack = MyStack()

        self.assertTrue(my_stack.empty())

        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)

        self.assertEqual(my_stack.top(), 3)

        my_stack.pop()

        self.assertEqual(my_stack.top(), 2)


if __name__ == "__main__":
    unittest.main()
