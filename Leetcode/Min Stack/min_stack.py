# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
"""
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
#Appraoch 1: One Stack
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.curr_min = float('inf')
        
#     def push(self, val):
#         if val < self.curr_min: self.curr_min = val
#         self.stack.append([val, self.curr_min])
#         return self.stack[-1][0]

#     def pop(self):
#         return self.stack.pop()[0]

#     def get_min(self):
#         return self.stack[-1][1]


#Approach 2: Two Stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        return self.stack[-1]

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]: self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        return self.min_stack[-1]

import unittest
class TestMinStack(unittest.TestCase):
    def test_generic(self):
        min_stack = MinStack()
        self.assertEqual(min_stack.push(3), 3)
        self.assertEqual(min_stack.push(4), 4)
        self.assertEqual(min_stack.push(1), 1)
        self.assertEqual(min_stack.push(5), 5)

        self.assertEqual(min_stack.get_min(), 1)
        self.assertEqual(min_stack.pop(), 5)

if __name__ == "__main__": unittest.main()