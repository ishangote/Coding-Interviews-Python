# 225. Implement Stack using Queues

> Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
>
> Implement the MyStack class:
>
> - `void push(int x)` Pushes element x to the top of the stack.
> - `int pop()` Removes the element on the top of the stack and returns it.
> - `int top()` Returns the element on the top of the stack.
> - `boolean empty()` Returns true if the stack is empty, false otherwise.
>
> Notes:
>
> You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
> Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

> Constraints:
>
> - 1 <= x <= 9
> - At most 100 calls will be made to push, pop, top, and empty.
> - All the calls to pop and top are valid.

## Examples

Example 1:

```
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

## Solution

```
Example:

->
q1 = []
q2 = []

push(1)
->
1.
q1 = []
q2 = [1]

2.
q1 = [1]
q2 = []


push(2)
->
1.
q1 = [1]
q2 = [2]

2.
q1 = []
q2 = [1, 2]

3.
q1 = [1, 2]
q2 = []

push(3)
1.
q1 = [1, 2]
q2 = [3]

2.
q1 = []
q2 = [1, 2, 3]

3.
q1 = [1, 2, 3]
q2 = []

pop()
q1.pop() => 3

**Algorithm**:
push(x)
1. Enqueue x to q2
2. Dequeue all elements of q1 and enqueue them in q2
3. Swap q1 and q2

```
