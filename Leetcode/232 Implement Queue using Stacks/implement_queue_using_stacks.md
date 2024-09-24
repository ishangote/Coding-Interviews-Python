# 232. Implement Queue using Stacks

## Problem Statement

> Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
>
> Implement the MyQueue class:
>
> - `void push(int x)` Pushes element x to the back of the queue.
> - `int pop()` Removes the element from the front of the queue and returns it.
> - `int peek()` Returns the element at the front of the queue.
> - `boolean empty()` Returns true if the queue is empty, false otherwise.

> Notes:
>
> - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
> - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

> Constraints:
>
> - 1 <= x <= 9
> - At most 100 calls will be made to push, pop, peek, and empty.
> - All the calls to pop and peek are valid.

## Examples

Example 1:

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

## Solution

```
Example 1:

stack1 = []
stack2 = []

------------------------
push(1)

stack1 = []
stack2 = [1]

stack1 = [1]
stack2 = []

------------------------
push(2)

* while stack1 is not empty put all elements in stack 2
stack1 = [1]
stack2 = []

stack1 = []
stack2 = [1]

* push 2 to top of the stack2
stack1 = []
stack2 = [1, 2]

* while stack2 is not empty put all elements to stack1
stack1 = [2, 1]
stack2 = []

------------------------
push(3)

stack1 = [2, 1]
stack2 = []

stack1 = []
stack2 = [1, 2]

stack1 = []
stack2 = [1, 2, 3]

stack1 = [3, 2, 1]
stack2 = []

...

Algorithm (push):
1. append element to stack2
2. while stack1 is not empty, pop element from stack1 and append to stack2
3. swap pointers for stack1 and stack2
```
