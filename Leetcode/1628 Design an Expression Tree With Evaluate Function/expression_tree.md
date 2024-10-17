# 1628. Design an Expression Tree With Evaluate Function

## Problem Statement

> Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.
>
> Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression `4*(5-(7+2))` are represented in the array `postfix = ["4","5","7","2","+","-","*"]`.
>
> The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.
>
> A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '\*' (multiplication), and '/' (division).
>
> It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).
>
> Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?

> Constraints:
>
> - 1 <= s.length < 100
> - s.length is odd.
> - s consists of numbers and the characters '+', '-', '\*', and '/'.
> - If s[i] is a number, its integer representation is no more than 10<sup>5</sup>.
> - It is guaranteed that s is a valid expression.
> - The absolute value of the result and intermediate values will not exceed 10<sup>9</sup>.
> - It is guaranteed that no expression will include division by zero.

## Examples

Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram.png)

```
Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.
```

Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram2.png)

```
Input: s = ["4","5","2","7","+","-","*"]
Output: -16
Explanation: this expression evaluates to the above binary tree with expression 4*(5-(2+7)) = 4*(-4) = -16.
```

## Solution

### Expression Tree from Postfix

```
Example 1:

postfix = ["3","4","+","2","*","7","/"]
stack = []


postfix = ["3","4","+","2","*","7","/"]
            ^
stack = [3]

------------------

postfix = ["3","4","+","2","*","7","/"]
                ^
stack = [3, 4]

------------------

postfix = ["3","4","+","2","*","7","/"]
                    ^                       * Pop both nodes from stack
stack = [3, 4]                              * Construct sub tree
                                                    +
                                                   / \
                                                  3   4
stack = [+]

------------------

postfix = ["3","4","+","2","*","7","/"]
                        ^
stack = [+, 2]

------------------

postfix = ["3","4","+","2","*","7","/"]
                            ^
stack = [+, 2]                                      *
                                                2       +
                                                       /  \
                                                      3    4
stack = [*]

------------------

postfix = ["3","4","+","2","*","7","/"]
                                ^
stack = [*, 7]

------------------

postfix = ["3","4","+","2","*","7","/"]
                                    ^                     /
stack = [*, 7]                                       *          7
                                                   2    +
                                                       / \
                                                      3    4

stack = [/]

Output: /
```

```
Example 2:

postfix: ["4","5","2","7","+","-","*"]
stack = []

------------------
postfix: ["4","5","2","7","+","-","*"]
           ^
stack = [4]
------------------
postfix: ["4","5","2","7","+","-","*"]
               ^
stack = [4, 5]
------------------
postfix: ["4","5","2","7","+","-","*"]
                   ^
stack = [4, 5, 2]
------------------
postfix: ["4","5","2","7","+","-","*"]
                       ^
stack = [4, 5, 2, 7]
------------------
postfix: ["4","5","2","7","+","-","*"]
                           ^                        +
stack = [4, 5, 2, 7]                              2   7

stack = [4, 5, +]
------------------
postfix: ["4","5","2","7","+","-","*"]              -
                               ^                5       +
stack = [4, 5, +]                                      2 7

stack = [4, -]
------------------
postfix: ["4","5","2","7","+","-","*"]              *
                                   ^             4      -
stack = [4, -]                                        5   +
                                                         2 7

stack = [*]

Output: *
```

## References

- Infix, Prefix, Postfix: https://www.youtube.com/watch?v=RY4GkLahbCI
- Infix to Postfix: https://www.youtube.com/watch?v=PAceaOSnxQs&ab_channel=Jenny%27sLecturesCSIT
- Binary Expression Tree: https://www.youtube.com/watch?v=2Z6g3kNymd0&t=117s&ab_channel=Jenny%27sLecturesCSIT
- Expression Tree from Postfix: https://www.youtube.com/watch?v=WHs-wSo33MM&t=301s&ab_channel=Jenny%27sLecturesCSIT
