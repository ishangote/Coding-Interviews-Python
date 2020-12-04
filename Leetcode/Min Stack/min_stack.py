# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
"""
Questions:
1. None values in stack? No
2. Duplicates? Yes

Examples:

stack = 
[(-3, -3), (0, min(0, -3)), (-2, min(-2, -3)), ]

push -3
push 0
push -2
getmin -> -3
pop -> -2
push -8
getmin -> -8
pop -> -8
getmin -> -3

"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        return None

    def push(self, x: int) -> None:
        if not self.min_stack: self.min_stack.append((x, x))
        else: self.min_stack.append((x, min(x, self.min_stack[-1][1])))
        return None

    def pop(self) -> None:
        if self.min_stack:
            return self.min_stack.pop()[0]

    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][0]
        return None
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][1]
        return None

if __name__ == "__main__":
    my_stack = MinStack()
    quit = False
    while not quit:
        opt = int(input("Enter 1 to push \nEnter 2 to pop \nEnter 3 to peek \nEnter 4 to get minimum \nEnter 5 to quit\n"))

        if opt == 1: 
            num = int(input("Enter a number"))
            print("RETURN: ")
            print(my_stack.push(num))
        elif opt == 2:
            print("RETURN: ")
            print(my_stack.pop())
        elif opt == 3:
            print("RETURN: ")
            print(my_stack.top())
        elif opt == 4:
            print("RETURN: ")
            print(my_stack.getMin())
        else: 
            quit = True