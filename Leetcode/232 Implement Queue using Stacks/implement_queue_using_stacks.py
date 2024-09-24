import unittest


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Time: O(n), where n => number of elements in the queue
    # Space: O(n), where n => number of elements in the queue
    def enqueue(self, element):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack2.append(element)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    # Time: O(1)
    def dequeue(self):
        return self.stack1.pop()

    # Time: O(1)
    def peek(self):
        return self.stack1[-1]

    # Time: O(1)
    def empty(self):
        return len(self.stack1) == 0


class TestMyQueue(unittest.TestCase):
    def test_my_queue(self):
        my_queue = MyQueue()

        my_queue.enqueue(1)
        self.assertEqual(my_queue.peek(), 1)

        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peek(), 1)

        my_queue.dequeue()
        self.assertEqual(my_queue.peek(), 2)


if __name__ == "__main__":
    unittest.main()
