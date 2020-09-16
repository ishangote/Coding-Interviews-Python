"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

"""
7 -> 2 -> 4 -> 3
     5 -> 6 -> 4
7    8    0    7

tmp = stack1.pop() + stack2.pop() + carry
stack3.append(tmp % 10)
carry = tmp // 10

carry = 0
stack1 = [7, 2, 4]
stack2 = [5, 6]
stack3 = [7]

carry = 1
stack1 = [7, 2]
stack2 = [5]
stack3 = [7, 0]

carry = 0
stack1 = [7]
stack2 = []
stack3 = [7, 0, 8]

stack3 = [7, 0, 8, 7]

l3

"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_two_nums(l1, l2):
    stack1, stack2 = [], []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next

    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    stack3 , carry = [], 0
    while stack1 or stack2:
        tmp = 0
        if stack1:
            tmp += stack1.pop()
        if stack2:
            tmp += stack2.pop()
        tmp += carry

        stack3.append(tmp % 10)
        carry = tmp // 10

    dummy = l3 = ListNode("DUMMY")

    if carry: stack3.append(carry)

    while stack3:
        l3.next = ListNode(stack3.pop())
        l3 = l3.next
    
    return dummy.next

"""
1   2   5
        6

[]
[]
carry = 0
tmp = 1
[]

d -> 1 -> 3 -> 1
              l3

s1
[]
s2
[]
tmp = 10
s3
[1]
carry = 1
"""