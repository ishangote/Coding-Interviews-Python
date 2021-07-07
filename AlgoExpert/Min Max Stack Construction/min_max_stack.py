"""
Examples:
push(5)
push(2)
push(7)

[(5, inf, -inf), (2, 5, 5), (7, 2, 5)]
min = 2
max = 7

pop()
[(5, inf, -inf), (2, 5, 5)]
min = 2
max = 5

Each element in stack must have the prev_min and prev_max stored
"""
import sys
class MinMaxStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_value = sys.maxsize
        self.max_value = -sys.maxsize
    
    def push(self, number):
        self.stack.append((number, self.min_value, self.max_value))
        self.min_value = min(self.min_value, number)
        self.max_value = max(self.max_value, number)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            self.min_value = popped[1]
            self.max_value = popped[2]
            return popped[0]

    def peek(self):
        if self.stack: return self.stack[-1][0]

    def getMin(self):
        return self.min_value

    def getMax(self):
        return self.max_value